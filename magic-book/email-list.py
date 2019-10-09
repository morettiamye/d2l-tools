import csv

file_path = "../test-files/"
file_name = "email.csv"

def emails():
    with open(file_path + file_name, "r") as csvfile:
        email_list = csv.reader(csvfile)
        for row in email_list:
            return row

# emails()
