import random
import time


names = ['John', 'Corey', 'Adam', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']


def people_list(number):
    result = []
    for i in range(number):
        person = {
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result


def people_generator(number):
    for i in range(number):
        person = {
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person


# t1 = time.process_time()
# people = people_list(1000000)
# t2 = time.process_time()

t1 = time.process_time()
people = people_generator(1000000)
t2 = time.process_time()

print('Time usage is {t1-t2}')
