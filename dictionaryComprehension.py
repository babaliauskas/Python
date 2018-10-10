# { __ : __ for __ in __ }

# Iterates over keys by default
# to iterate over keys and values using .items()


# number = { 
#   'a':1,
#   'b':2
# } 

# squared_numbers = {key: value ** 2 for key, value in number.items()}
# print(squared_numbers)


# str1 = 'ABC'
# str2 = '123'
# combo = {str1[i]: str2[i] for i in range(0, len(str1))}
# print(combo)

# person = {
#   "name": 'lukas',
#   'city': 'denver',
#   'last': 'babaliauskas'
# }

# upper_person = {k.upper(): v.upper() for k,v in person.items()}
# print(upper_person)

# list_numbers = [1,2,3,4,5]
# list_even_odd = {num:('even' if num % 2 == 0 else 'odd') for num in list_numbers}
# print(list_even_odd)

# upper_name_person = {(k.upper() if k == 'name' else k): v for k,v in person.items() }
# print(upper_name_person)


# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
# answer = {k:v for k,v in person}
# print(answer)


# answer2 = {char: 0 for char in 'aeiou'}
# print(answer2)


