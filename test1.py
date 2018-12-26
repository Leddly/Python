course = ['History', 'Math', 'Physics', 'CompSci']

# print('Art' in course)

for index, sub in enumerate(course, start=1):
    print(index, sub)

course_str = ', '.join(sorted(course))

new_list = course_str.split(', ')

print(course_str)

print(new_list)
