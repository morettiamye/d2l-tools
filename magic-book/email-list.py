import csv

email_file_path = "../test-files/"
email_file_name = "email.csv"

with open(email_file_path + email_file_name, "r") as csvfile:
    email_list = csv.reader(csvfile)
    for row in email_list:
        print(row)

