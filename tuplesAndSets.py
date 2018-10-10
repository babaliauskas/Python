#  - Describe, create and access tuples and sets
#  - Use built in methods to modify sets and access values in tuples
#  - Iterate over sets using loops and set comprehensions
#  - Compare and cotrast sets & tuples with lists & dictionaries
 


# Tuple:
#   - An ordered collection or grouping items
#   - numers = (1,2,3,4)
#   - it is immutable! cant be changed
#   - Tuples are faster than lists
#   - it makes your code safer
#   - Valid keys in a dictionary
#   - .items() return tuples

#   - .count() - returns the number of times a value appears in a tuple
#     - x = (1,2,3,3,3)
#     - x.count(1) # 1
#     - x.count(3) # 3

#   - index() - returns the index at which a value is found in a tuple  
#     - t = (1,2,3,3,3,4)
#     - t.index(1) # 0
#     - t.index(9) # ValueError

# locations = {
#   (35.623, 39.2342): 'New York',
#   (23.134, 23.432): 'San Francisco'
# }



# Sets: 
#   - Sets are like formal mathematical sets
#   - Sets do not have duplicate values
#   - Elements in sets arent ordered
#   - You cannot access items in a set by index
#   - Sets can be useful if you need to keep track of a collection of elements, but dont care about ordering, keys or values and duplicates.

# .add() - adds an elemnt to a set. if the element is already in the set, the set doesnt change

# .remove() - removes a value from the set - returns a KeyError if the value is not found

# .discard() - removes a value from the set - doesnt give a error if the value is not found

# .copy() - Creates a copy of the set

# .clear() - removes all the contents of the set



#  - set union
#   -  To generate a set with all unique numbers
#   -  num = {1,2,3,4,5,1,1,1,1,2}
#   -  num2 = {3,4,6,7,8,1}
#   -  print(num | num2) # {1,2,3,4,5,6,7,8}

#  - set intersections
#   - To generate a set with numbers who are in both sets
#   - print(num & num2) # {1,3,4}



# s = set({1,2,3,4,5,6,6,6}) # {1,2,3,4,5,6}
# s = {1,4,5, 'a', 2.333}
# 4 in s # True
# 8 in s # False

# numbers = {1,2,3,4}

# for i in numbers:
#   print(i)
#   # 1
#   # 2
#   # 3
#   # 4 

# cities = ['daugai', 'alytus', 'vilnius', 'kaunas', 'klaipeda', 'daugai', 'daugai', 'vilnius', 'vilnius', 'vilnius']
# print(set(cities))
# print(len(list(set(cities))))