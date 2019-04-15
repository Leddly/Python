from operator import attrgetter


class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f'{self.name}, {self.age}, {self.salary}'


def esort(employee):
    return employee.name


e1 = Employee('Carl', 38, 80000)
e2 = Employee('Sarah', 32, 46000)
e3 = Employee('John', 43, 90000)

employees = [e1, e2, e3]

print(sorted(employees, key=lambda e: e.name, reverse=False))
print(sorted(employees, key=esort, reverse=False))
print(sorted(employees, key=attrgetter('name'), reverse=False))

li = [-6, -5, -4, 1, 2, 3]
s_li = sorted(li, key=abs)

print(s_li)
