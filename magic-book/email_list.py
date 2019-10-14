import csv

# Change File Path and Course file name here
file_path = "../test-files/"
file_name = "email.csv"

def emails():
    with open(file_path + file_name, newline="") as csvfile:
        email_list = csv.reader(csvfile, delimiter=" ", quotechar="|")
        for row in email_list:
            print(",".join(row))

# emails()
