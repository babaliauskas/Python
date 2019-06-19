# Raise Your Own Exception

# raise ValueError('invalid value')
# raise NameError('Invalid name')

##########################


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
divide(1, 0)
