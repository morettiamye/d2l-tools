import csv

# Change File Path and Course file name here
file_path = "../test-files/"
file_name = "courses.csv"

def open_courses():
    with open(file_path + file_name, "r") as csvfile:
        course_offerings = csv.reader(csvfile, delimiter=" ")
        for row in course_offerings:
            print(",".join(row))

# open_courses()
