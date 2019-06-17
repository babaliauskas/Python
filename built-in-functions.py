# One line, no name function

#########################


def decrement_list(numbers):
    answer = list(map(lambda num: num - 1, numbers))
    return answer


decrement_list([2, 3, 4])

#############################

names = ['lukas', 'mode', 'linas', 'benas']

filtered_names = list(filter(lambda name: name[0] == 'l', names))

# print(filtered_names)

################################

users = [
    {"username": "lukas", "tweets": ["I love cake", "I love dogs"]},
    {"username": "mode", "tweets": []},
    {"username": "Siga", "tweets": ["I love cake", "I love dogs"]},
    {"username": "benas", "tweets": ["I love cake", "I love dogs"]},
    {"username": "linas", "tweets": []}
]

# inactive_users = list(filter(lambda user: len(user['tweets']) == 0, users))
# OR
inactive_users = list(filter(lambda user: not user["tweets"], users))

# [] '' 0  is false

# print(inactive_users)

######################################

usernames = list(map(lambda names: names['username'],
                     filter(lambda fnames: not fnames['tweets'], users)))

# print(usernames)

######################################

# inactive_users2 = [user for user in users if not user['tweets']]

# print(inactive_users2)

#######################################

string_list = ['lukas', 'benas', 'mode']


def is_string(lst):
    return all(type(l) == str for l in lst)


print('IS STRING: ', is_string(string_list))
