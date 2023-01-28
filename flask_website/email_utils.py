from csv import writer

email = ''''''
email = email.lower()
email = email.replace(' ', ',')

result = 0



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
print(new_row)
new_row['result\n'] = result

list_values = [new_row.values()]



################################################
# write
################################################
with open("email_data.csv", "a", newline='') as file:
    # Create a CSV writer object
    writer = writer(file)
    # Write the values to the CSV file
    writer.writerows(list_values)