from functools import wraps
from time import time


def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f"Executing {fn.__name__}")
        print(f"Time Elapsed: {end_time - start_time}")
        return result
    return wrapper


@speed_test
def sum_nums_gen():
    return sum(x for x in range(90000000))


@speed_test
def sum_nums_list():
    return sum([x for x in range(90000000)])


###########################

def log_function_data(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """I AM WRAPPER FUNCTION"""
        print(f"you are about to call {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper


@log_function_data
def add(x, y):
    """Adds two numbers together"""
    return x + y


#########################################

def be_polite(fn):
    def wrapper():
        print('blllaaaa')
        fn()
        print('hmmm')
    return wrapper


@be_polite
def greet():
    print('My name is John')
