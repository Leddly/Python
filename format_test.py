person = {'name': 'Jenn', 'age': 23}

# sentence = 'My name is {0[name]} and I am {0[age]} years old'.format(person)
# sentence = 'My name is {0} and I am {1} years old'.format(person['name'], person['age'])
# sentence = 'My name is {} and I am {} years old'.format(person['name'], person['age'])
sentence = 'My name is {name} and I am {age} years old'.format(**person)

print(sentence)

for i in range(1, 11):
    sentence = f'The value is {i:03}'
    print(sentence)

pi = 3.14195265

print(f'Pi is {pi:.3f}')
print(f'Data is {1000*30:,.3f}')
