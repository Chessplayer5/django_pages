import glob
import csv
from datetime import datetime
from dateutil.relativedelta import relativedelta

write_csv = False
py_files = glob.glob("*_cust_class.py")

if not py_files:
    print(
        "No assignment 6 class files found. Confirm the file is present and named correctly"
    )
elif len(py_files) > 1:
    write_csv = True
    grades = open("a6_grades.csv", "w", newline="")
    grade_writer = csv.writer(grades)
    grade_writer.writerow(["Name", "PY_File", "Grade"])


for py_file in py_files:
    student_grade = []
    grade = 5
    paws_id = py_file.replace("_cust_class.py", "")

    with open(py_file) as file:
        student_grade.append(py_file)
        for line in file:
            if "def __init__" in line:
                grade += 5
            if "def full_name" in line:
                grade += 5
            if "def age" in line:
                grade += 5
            if "def adult" in line:
                grade += 5
            if "def to_json" in line:
                grade += 5

    try:
        py_file = py_file.replace(".py", "")
        a6 = __import__(py_file)

        dob = datetime(1994, 8, 15).date()
        age = relativedelta(datetime.today(), dob).years
        try:
            c = a6.Customer(
                91,
                "Robert",
                "Lewis",
                dob.strftime("%Y-%m-%d"),
                "Wilsonborough",
                "MT",
                "53741",
            )
            grade += 15
        except:
            print("There is an issue with your __init__ function")

        try:
            if c.student_name:
                grade += 5
            else:
                print("Variable student_name does not exist")
        except:
            print("Variable student_name does not exist")

        student_grade.insert(0, c.student_name)

        if (c.full_name()) == "Robert Lewis":
            grade += 10
        else:
            print("Your full_name function is not correct.")

        if c.age() == relativedelta(datetime.today(), dob).years:
            grade += 10
        else:
            print("Your age function is not correct.")

        if (c.adult()) == True:
            grade += 15
        else:
            print("Your adult function is not correct.")

        # try:
        c_dict = c.to_json()
        if (
            c_dict["adult"]
            and (c_dict["city"] == "Wilsonborough")
            and (c_dict["zip"] == "53741")
        ):
            grade += 15
        else:
            print("Your to_json function is not correct.")
        # except:
        #     print("Your to_json function is not correct.")

        print("The grade for " + c.student_name + " should be: " + str(grade))
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
