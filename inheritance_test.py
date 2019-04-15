class Employee(object):

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@gmail.com'

    def __str__(self):
        return(self.first + ' ' + self.last)

    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, p_lang):
        super().__init__(first, last, pay)
        self.p_lang = p_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('====>' + emp.__str__())


dev1 = Developer('Corey', 'Schafer', 60000, 'Python')
dev2 = Developer('Test', 'Employee', 70000, 'Java')

mgr1 = Manager('Sue', 'Smith', 80000, [dev1])

print(mgr1.email)
mgr1.print_emp()
print('\n')
mgr1.add_emp(dev2)
mgr1.print_emp()

print(isinstance(mgr1, Employee))

# print(dev1.email, dev1.p_lang)
# print(dev2.email, dev2.p_lang)


# print(dev1.pay)
# dev1.apply_raise()
# print(dev1.pay)

# print(emp1.pay)
# emp1.apply_raise()
# print(emp1.pay)
