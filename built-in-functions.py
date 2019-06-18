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


# print('IS STRING: ', is_string(string_list))

##########################################

# SORTING

# sorted() return a copy

# nums = [2, 5, 1, 3]
# nums.sort()  # - nums = [1, 2, 3, 5]

# nums2 = [5, 4, 7, 1]
# sorted(nums)  # - return copy of nums2 and sort


users2 = [
    {"username": "lukas", "tweets": ["I love cake", "I love dogs"]},
    {"username": "mode", "tweets": []},
    {"username": "Siga", "tweets": ["I love cake", "I love dogs"]},
    {"username": "benas", "tweets": ["I love cake", "I love dogs"]},
    {"username": "arminas", "tweets": []}
]

# print('Sorting: ', sorted(users2, key=lambda user: user['username']))
# print('Sorting: ', sorted(
#     users2, key=lambda user: len(user['tweets']), reverse=True))


#############################################

# MAX

# Return the largest item in an iterable or the largest of two or more arguments

# MIN

# does the same like max just oposit

names2 = ['lukas', 'mode', 'siga', 'arminas', 'zygimantas']

# longest_name = max(names2, key=lambda n: len(n))
# print('Longest Name: ', longest_name)

# sortest_name = min(names2, key=lambda n: len(n))
# print('Sortest Name: ', sortest_name)

songs = [
    {'title': 'happy birthday', 'playcount': 1},
    {'title': 'Survive', 'playcount': 99},
    {'title': 'Toxic', 'playcount': 23},
    {'title': 'YMCA', 'playcount': 52}
]

# min_song_title = min(songs, key=lambda s: s['playcount'])['title']
# print('Min Song Title: ', min_song_title)


max_song_title = max(songs, key=lambda s: s['playcount'])['title']
print('Max Song Title: ', max_song_title)


#############################################

# reversed()

# return a copy of reverse iterator

for x in reversed(range(0, 10)):
    print(x)


############################################

# abs

# Return the absolute value of a number. The argument may be an integer or a floating point number.
# works only with numbers

abs(-2)  # 2
abs(2)  # 2
abs(-3.222)  # 3.222
abs(3.222)  # 3.222


############################################

# sum

# Takes an iterable and an optional start.
# Returns the sum of start and the items of an iterable from left to right and returns the total
