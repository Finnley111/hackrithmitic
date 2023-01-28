from csv import writer

def email_data(text):
    email = text.lower()
    email = text.replace(' ', ',')
    filename = "email_data.csv"
    fobj = open(filename, "r")
    new_row = {}

    first_line = ""
    for line in fobj:
        first_line = line
        break
    fobj.close()

    fl_list = line.split(',')

    for word in fl_list:
        new_row[word] = email.count(word)
    del new_row['result\n']

    list_values = new_row.values()
    print(len(list_values))
    return list(list_values)

email = '''Hi Finnley,

Congratulations, you have passed the screening stage for the Data Scientist (Risk Research) Intern position and will move on to the next step of the process, our technical test.

The test will take at most 120 minutes. Please ensure you use the same email on the test as you did on your application so we can credit you with your results. You will receive an invitation from HackerRank shortly after receiving this email.

Please ensure you take the test within 72 hours of receiving it. The system takes some time to send the test link, but if you do not receive it by the end of the day, please respond to this email, and I will re-send it.

Any questions? Please join our internship LinkedIn Network for the fastest response time, and post your questions in the group.

Best of luck!

Eleanor Hawkins
Campus Recruitment Team
GeoComply'''
print(email_data(email))
