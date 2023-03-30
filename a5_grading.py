import glob
import csv
from datetime import date
from dateutil.relativedelta import relativedelta
from dateutil.parser import isoparse


write_csv = False
py_files = glob.glob("*_assignment5.py")
if not py_files:
    print(
        "No assignment 5 files found. Confirm the file is present and named correctly"
    )
elif len(py_files) > 1:
    write_csv = True
    grades = open("a5_grades.csv", "w", newline="")
    grade_writer = csv.writer(grades)
    grade_writer.writerow(["Name", "PY_File", "CSV_File", "Grade"])

for py_file in py_files:
    student_grade = []
    grade = 5
    paws_id = py_file.replace("_assignment5.py", "")
    print(paws_id)
    customer_sqlite = False
    db_connect = False
    with open(py_file) as file:
        student_grade.append(py_file)
        for line in file:
            if "sqlite:///customer.sqlite" in line:
                customer_sqlite = True
            if customer_sqlite and ("connect()" in line):
                db_connect = True
                grade += 5
            if db_connect and ("close()" in line):
                db_connect = False
                grade += 5
            if "def main" in line:
                grade += 10
            if "def full_name" in line:
                grade += 10
            if "def age" in line:
                grade += 10

    try:
        py_file = py_file.replace(".py", "")
        a5 = __import__(py_file)
        try:
            if a5.student_name:
                grade += 5
            else:
                print("Variable student_name does not exist")
        except:
            print("Variable student_name does not exist")

        csv_file = glob.glob(paws_id + "_assignment5.csv")
        student_grade.append(paws_id + "_assignment5.csv")
        if csv_file:
            grade += 5
            with open(paws_id + "_assignment5.csv", "r") as file:
                csv_reader = csv.reader(file)
                header = next(csv_reader)
                print(header)
                if set(["Customer ID", "Name", "Age"]).issubset(header):
                    grade += 5
                else:
                    print("Header row is not correct in the csv file")
                num_rows = len(list(csv_reader))
                print("num_rows:", num_rows)
                if num_rows == 99:
                    grade += 10
                else:
                    print("There should be a header and 99 customers in the csv file")
        else:
            print("Output file " + paws_id + "_assignment5.csv" + " does not exist")

        student_grade.insert(0, a5.student_name)

        if (a5.full_name("Bob", "Smith")) == "Bob Smith":
            grade += 15
        else:
            print("Your full_name function is not correct.")

        dob = "2005-05-08"

        if (a5.age(dob)) == relativedelta(date.today(), isoparse(dob).date()).years:
            grade += 15
        else:
            print("Your age function is not correct.")

        print("The grade for " + a5.student_name + " should be: " + str(grade))
        if grade >= 90:
            print("Another 'A'! Keep up the good work.")

        student_grade.append(grade)
        if write_csv:
            grade_writer.writerow(student_grade)
        else:
            print(student_grade)

    except Exception as e:
        print("There appears to be syntax errors in your code.")
        print(e)

        student_grade.append("code errors")
        if write_csv:
            grade_writer.writerow(student_grade)
        else:
            print(student_grade)

if write_csv:
    grades.close()
