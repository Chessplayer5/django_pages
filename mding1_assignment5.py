import sqlalchemy as db
from datetime import datetime
from dateutil.relativedelta import relativedelta
import csv

student_name = "Matthew Ding"


def main():
    engine = db.create_engine("sqlite:///customer.sqlite")
    connection = engine.connect()
    results = connection.execute("select * from customer")

    out_file = open("mding1_assignment5.csv", "w", newline="")
    csv_writer = csv.writer(out_file)
    csv_writer.writerow(["Customer ID", "Name", "Age"])

    for row in results:
        # print(row)
        # print(full_name(row[1], row[2]), age(row[3]) )
        csv_writer.writerow([full_name(row[1], row[2]), age(row[3])])

    connection.close()
    out_file.close()


def full_name(fname, lname):
    return fname + " " + lname


def age(d):
    dob = datetime.strptime(d, "%Y-%m-%d")
    today = datetime.today()
    age = relativedelta(today, dob)
    return age.years


main()
