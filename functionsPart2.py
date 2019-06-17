# OBJECTIVES:
#  - Use the * and ** operator as parameters to a function outside of a function
#  - Leverage dictionary and tuple unpacking to create more flexible functions


# Single *args:
#  - a special operator we can pass to functions
#  - Gathers remaining arguments as a tuple
#  - this is just a parameter - ou can call it whatever you want!

def sum_all_nums(*args):
    total = 0
    for num in args:
        total += num
    return total


print('sum_all_nums: ', sum_all_nums(4, 3, 2, 5, 6, 7))

#############################


def sum_all_nums2(num1, *args):
    print(num1)  # 2
    total = 0
    for num in args:
        total += num
    return total


print('sum_all_nums2: ', sum_all_nums2(2, 2, 3, 4, 5, 5, 6, 7))

#############################


def ensure_correct_info(*args):
    if 'Colt' in args and 'Steele'in args:
        return 'Welcome back Colt'
    return 'Not sure who you are...'


print('ensure_correct_info: ', ensure_correct_info(1, 2, True, "Steele", 'Colt'))


# Double star **kwargs:
#   - A special operator we can pass to a function
#   - Gathers remaining keyword arguments as a dictionary
#   - This is just a parameter - you can call it whatever you want!

def fav_colors(**kwargs):
    return kwargs


print('fav_colors: ', fav_colors(colt='purple', ruby='red', ethel='teal'))

#############################


def fav_colors2(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}'s favoite color is {v}")


print('fav_colors2: ', fav_colors2(benas='purple', mode='red', lukas='teal'))

###############################


def special_greeting(**kwargs):
    if "David" in kwargs and kwargs['David'] == 'special':
        return 'You get a special greeting Davif!'
    elif 'David' in kwargs:
        return f"{kwargs['David']} David!"
    return 'Not sure who this is...'


print('special_greeting: ', special_greeting(David='Hello'))
print('special_greeting: ', special_greeting(Bob='Hello'))
print('special_greeting: ', special_greeting(David='special'))


# Passing list and tuples into *args:
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total


nums = [1, 2, 3, 4, 5, 6, 67, 7]
print('Passing list/tuples *args: ', sum_all(*nums))

# Passing list and tuples into **kwargs:


def display_names(first, second):
    return f"{first} says hello to {second}"


names = {'first': 'Colt', 'second': 'Rusty'}
print('Passing dictionary: ', display_names(**names))

#################################


def add_and_multiply_numbers(a, b, c, **kwargs):
    print()
    return a + b * c


data = dict(a=1, b=2, c=3)
print('Unpacking dict and passing to a fn(): ',
      add_and_multiply_numbers(**data))

#################################

# case number

# utah decloration page case number.  to mva write fax: 14107687073

# 2610 amos clark in. apt 401 jessup md 20794
