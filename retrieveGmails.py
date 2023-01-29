from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import csv
import base64
from bs4 import BeautifulSoup


# Use the credentials to build the Gmail service
creds = Credentials(token)
service = build('gmail', 'v1', credentials=creds)

# Retrieve all emails from the inbox
result = service.users().messages().list(userId='me', maxResults=200).execute()
messages = result.get('messages', [])

user_id =  'me'
label_id_one = 'INBOX'
label_id_two = 'UNREAD'

final_list = []

for mssg in messages:
    temp_dict = {}
    m_id = mssg['id'] # get id of individual message
    message = service.users().messages().get(userId=user_id, id=m_id).execute() # fetch the message using API
    payld = message['payload'] # get payload of the message 
    headr = payld['headers'] # get header of the payload

    

    if 'parts' in payld.keys():
        mssg_parts = payld['parts']
        part_one  = mssg_parts[0] 
        part_body = part_one['body'] 
        if part_body.get('attachmentId'): #checking if the message body is attachment
            attachment = service.users().messages().attachments().get(id=part_body['attachmentId'],userId=user_id, messageId=m_id).execute()
            data = attachment.get('data')
            if data:
                clean_two = base64.b64decode (data)
                soup = BeautifulSoup(clean_two , "html.parser" )
                mssg_body = soup.get_text()
                temp_dict['Message_body'] = mssg_body
                final_list.append(temp_dict)
    else:
        part_data = part_body['data'] 
        clean_one = part_data.replace("-","+") 
        clean_one = clean_one.replace("_","/") 
        clean_two = base64.b64decode (bytes(clean_one, 'UTF-8')) 
        soup = BeautifulSoup(clean_two , "html.parser" )
        mssg_body = soup.get_text()
        temp_dict['Message_body'] = mssg_body
        final_list.append(temp_dict)
else:
    temp_dict['Message_body'] = "No message body found"
    final_list.append(temp_dict)

# Open a CSV file to write the email data
with open('emails.csv', 'w', encoding='utf-8', newline="") as csvfile:
    fieldnames = ['Subject','Message_body']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter = ',')
    for val in final_list:
        writer.writerow(val)
    writer.writeheader()
