import sqlalchemy as db
from datetime import datetime
from dateutil.relativedelta import relativedelta


class Customer:
    student_name = "Matthew Ding"

    # (7, 'Oscar', 'Doyle', '1995-02-02', 'South Cindy', 'VT', '04481')

    def __init__(self, id, fname, lname, dob, city, state, zip):
        self.id = id
        self.first_name = fname
        self.last_name = lname
        self.dob = dob
        self.city = city
        self.state = state
        self.zip = zip

    def full_name(self):
        return self.first_name + " " + self.last_name

    def age(self):
        dob = datetime.strptime(self.dob, "%Y-%m-%d")
        today = datetime.today()
        age = relativedelta(today, dob)
        return age.years

    def adult(self):
        age = self.age()
        if age >= 18:
            return True
        else:
            return False

    def to_json(self):
        j = {}
        j.update(self.__dict__)
        j["age"] = self.age()
        j["adult"] = self.adult()
        j["full_name"] = self.full_name()
        return j
