import glob
import csv

write_csv = False
py_files = glob.glob("*_assignment4.py")
if not py_files:
    print(
        "No assignment 4 files found. Confirm the file is present and named correctly"
    )
elif len(py_files) > 1:
    write_csv = True
    grades = open("a4_grades.csv", "w", newline="")
    grade_writer = csv.writer(grades)
    grade_writer.writerow(["Name", "File", "num_for_loops", "open_files", "Grade"])

for py_file in py_files:
    student_grade = []
    grade = 5
    num_for_loops = 0
    num_open_files = 0
    open_csv = True
    open_txt = True
    paws_id = py_file.replace("_assignment4.py", "")
    with open(py_file) as file:
        student_grade.append(py_file)
        for line in file:
            if ("open" in line) and ("mpg.csv" in line):
                open_csv = True
                num_open_files += 1
                if "with" in line:
                    open_csv = False
                    num_open_files -= 1
            # if open_csv and ('close' in line):

            if ("open" in line) and ("txt" in line):
                open_txt = True
                num_open_files += 1
                if "with" in line:
                    open_txt = False
                    num_open_files -= 1

            if "close()" in line:
                # print(line)
                open_csv = False
                open_txt = False
                num_open_files -= 1

            if line.strip().startswith("for "):
                num_for_loops += 1
                print(line)

        if num_for_loops > 1:
            print("Too many 'for loops': " + py_file)
            grade -= (num_for_loops - 1) * 10
        student_grade.append(num_for_loops)

        if open_csv:
            print("CSV file was not closed")
            grade -= 10
        # student_grade.append(open_csv)

        if open_txt:
            print("TXT file as not closed")
            grade -= 10
        # student_grade.append(open_txt)

        print(num_open_files)
        if num_open_files != 0:
            print("Check that your CSV and TXT files are properly opened & closed")
        student_grade.append(num_open_files)

    try:
        py_file = py_file.replace(".py", "")
        a4 = __import__(py_file)
        try:
            if a4.student_name:
                grade += 5
            else:
                print("Variable student_name does not exist")
        except:
            print("Issue with student_name")
        student_grade.insert(0, a4.student_name)

        txt_file = glob.glob(paws_id + "_assignment4.txt")
        if txt_file:
            grade += 20
        else:
            print("Output file " + paws_id + "_assignment4.txt " + "does not exist")

        try:
            if round(a4.avg_city, 2) == 16.86:
                grade += 15
            else:
                print("Your avg_city is not correct.")
        except:
            print("Issue with avg_city")

        try:
            if round(a4.avg_hwy, 2) == 23.44:
                grade += 15
            else:
                print("Your avg_hwy is not correct.")
        except:
            print("Issue with avg_hwy")

        try:
            if a4.ford_hwy == 19.36:
                grade += 20
            else:
                print("Your ford_hwy is not correct.")
        except:
            print("Issue with ford_hwy")

        try:
            if a4.suv_city == 13.5:
                grade += 20
            else:
                print("Your suv_city is not correct.")
        except:
            print("Issue with suv_city")

        student_grade.append(grade)
        if write_csv:
            grade_writer.writerow(student_grade)
        else:
            print(student_grade)

        print("The grade for " + a4.student_name + " should be: " + str(grade))
        if grade >= 90:
            print("Another 'A'! Keep up the good work.")

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
