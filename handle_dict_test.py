student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

student['phone'] = '555-5555'

student.update({'name': 'Jane', 'age': 26})

del student['age']

# = student.pop('age')

print(student.get('phone'))
print(student.get('addr', 'not found'))
print(student)
