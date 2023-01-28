from csv import writer

email = "APPLICATION"
email = email.lower()

filename = "email_data.csv"
fobj = open(filename, "r")
new_row = {}

first_line = ""
for line in fobj:
    first_line = line

fl_list = line.split(',')

for word in fl_list:
    new_row[word] = email.count(word)

list_values = new_row.values()

fobj.close()

################################################
# write
################################################
with open('email_data.csv', 'a') as f_object:
 
    # Pass this file object to csv.writer()
    # and get a writer object
    writer_object = writer(f_object)
 
    # Pass the list as an argument into
    # the writerow()
    writer_object.writerow(list_values)
 
    # Close the file object
    f_object.close()