class Employee(object):

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first+'.'+last+'@gmail.com'

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Deleted.')
        self.first = None
        self.last = None


emp = Employee('Corey', 'Schafer')

print(emp.fullname)

emp.fullname = 'Leddy Lee'

print(emp.fullname)

del emp.fullname

print(emp.fullname)
