# Raise Your Own Exception

# raise ValueError('invalid value')
# raise NameError('Invalid name')

# \


def colorize(text, color):
    colors = ('red', 'blue', 'green')
    if type(text) is not str:
        raise TypeError('Text must be instance of string')
    if color not in colors:
        raise ValueError('Invalid color')
    print(f"Printed {text} in {color}")


# colorize('car', 'yellow')
# colorize(34, 'red')

###########################################

# try:
#     foo
# except:
#     print('PROBLEM!!!!!!')
# print('The end')


def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None


d = {'name': 'Lukas'}
# print('Get error: ', get(d, 'name'))

#################################################

# while True:
#     try:
#         num = int(input('Please enter a number: '))
#     except ValueError:
#         print("That's not a number")
#     else:
#         print("I'm in the else!")
#         break
#     finally:
#         print("RUNS NO MATTER WHAT!")
# print('Good Job!')

##################################################


# def divide(a, b):
#     try:
#         result = a/b
#     except ZeroDivisionError:
#         print("don't divide by zero please!")
#     except TypeError as err:
#         print('a and b must be ints or floats')
#         print(err)
#     else:
#         print(f'{a} divided by {b} is {result}')


# divide(1, 2)
# divide(1, 'a')

####################################

def divide(a, b):
    try:
        result = a/b
    except (ZeroDivisionError, TypeError) as err:
        print('something went wrong!')
        print(err)
    else:
        print(f'{a} divided by {b} is {result}')


# divide(1, 2)
# divide(1, 0)

######################################
# import pdb
first = 'First'
second = 'Second'
# pdb.set_trace()
result = first + second
third = 'Third'
result += third
print(result)

#############################################


def add_numbers(a, b, c):
    # import pdb; pdb.set_trace()
    return a + b + c


# add_numbers(1, 2, 3)

# Commonly on one line:
#import pdb; pdb.set_trace()

# Common PDB Commands:
# l (list)
# n (next line)
# p (print)
# c (continue - finishes debugging)


##############################

def divide2(num1, num2):
    try:
        result = num1 / num2
    except TypeError:
        return 'Please provide two integers or floats'
    except ZeroDivisionError:
        return 'Please do not divide by zero'
    else:
        return result


divide2(4, 2)
