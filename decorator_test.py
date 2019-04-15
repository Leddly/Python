

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("Wrapper executed this before {}".format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function


class decorator_class(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print("Class method executed this before {}".format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@decorator_function
def display():
    print('Display function ran')


@decorator_function
def display_info(name, age):
    print('{} {}'.format(name, age))


@decorator_class
def display_infor(name, age):
    print('{} {}'.format(name, age))


display_info('Jonh', 26)
display()
display_infor('Tom', 27)
