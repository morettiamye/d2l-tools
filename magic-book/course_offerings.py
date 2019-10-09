import csv

file_path = "../test-files/"
file_name = "courses.csv"

def open_courses():
    with open(file_path + file_name, "r") as csvfile:
        course_offerings = csv.reader(csvfile)
        for row in course_offerings:
            return row

# open_courses()
