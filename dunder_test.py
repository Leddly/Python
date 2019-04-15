class Employee(object):

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@gmail.com'

    def __str__(self):
        return(self.first + ' ' + self.last)

    def __repr__(self):
        return("Employee {}, {}, {}".format(self.first, self.last, self.pay))

    def __add__(self, other):
        return self.pay + other.pay

    def __le__(self):
        return len(self.__str__())


emp1 = Employee('Corey', 'Schafer', 60000)
emp2 = Employee('Test', 'Employee', 70000)

print(emp1)
print(emp1+emp2)
print(emp1.__le__())
