import datetime


class Employee(object):

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@gmail.com'
        Employee.num_of_emps += 1

    def __str__(self):
        return(self.first + self.last)

    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, string):
        first, last, pay = string.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True


emp3 = 'John-Doe-70000'

emp1 = Employee('Corey', 'Scharfer', 50000)
emp2 = Employee('Test', 'Employee', 60000)
emp3 = Employee.from_string(emp3)

Employee.set_raise_amount(1.05)
# emp1.set_raise_amount(1.05)
# emp2.set_raise_amount(1.05)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
print(emp3.__str__())

my_date = datetime.date(2019, 10, 23)

print(Employee.is_workday(my_date))
