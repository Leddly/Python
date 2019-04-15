import os

my_list = [1, 2, 3, 4, 5, 6]

# non Pythonic
if len(my_list) > 5:
    print(my_list[5])

# Pythonic
try:
    print(my_list[5])
except Exception as e:
    print(e)

# Race condition
if os.access('File name', os.R_OK):
    with open('File name', 'r') as f:
        print(f.read())
else:
    print('File cannot be accessed')

# No Race condition
try:
    f = open('File name', 'r')
except Exception as e:
    print(e)
else:
    with f:
        print(f.read())
