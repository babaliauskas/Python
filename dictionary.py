
.clear() - clears all the key and valyes in a dictionary
         - d = dict(a=1,b=2)
         - d.clear() # {}

.copy()  - makes a copy/clone of a dictionary
         - d = dict(a=1,b=2)
         - c = d.copy() # {'a': 1, 'b': 2}
         - c is d # false. stores in different place of memory

{}.fromkeys() - creates key-value pairs from comma separated values
              - {}.fromkeys('a', 'b') # {'a': 'b'}
              - {}.fromkeys('a', [1,2,3,4,5]) # {'a': [1,2,3,4,5]}

.get() - retrieves a key in an object and return None instead of a KeyError if the key
       - does not exist
       - d = dict(a=1,b=2)
       - d['a'] # 1 
       - d.get('a') # 1

.pop() - Takes a single argument corresponding to key and removes that key-value pair
       - from the dictionary. Returns the value corresponding to the key that was removed
       - d = { 'a': 1, 'b': 2}
       - d.pop('a') # returns the value that was removed - 1

.popitem() - removes a random key in a ditionary
           - popitems takes no arguments

.update() - update keys and values in a dictionary with another set of key value  pairs





# cat = { 
#   "name": "blue", 
#   "age": 3.5, 
#   "isCute": True 
# }
# print(cat)

# cat2 = dict(name="kitty", age=0.5)
# print(cat2['name'])


# # Get Values
# for v in cat.values():
#   print(v)

# # Get Keys
# for k in cat.keys():
#   print(k)

# # Get Values and Keys
# for key, value in cat.items():
#   print(key,value)


# donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)


# total_donations = 0
# for v in donations.values():
#     total_donations += int(v)
  
# # print(total_donations)



# new_user = {}.fromkeys(['name', 'score', 'email'], 'unknown')
# print(new_user)


# This code picks a random food item:






######################################################################

# from random import choice #DON'T CHANGE!
# food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

# #DON'T CHANGE THIS DICTIONARY EITHER!
# bakery_stock = {
#     "almond croissant" : 12,
#     "toffee cookie": 3,
#     "morning bun": 1,
#     "chocolate chunk cookie": 9,
#     "tea cake": 25
# }

# # YOUR CODE GOES BELOW:
# if food in bakery_stock:
#   print(f'{bakery_stock[food]}')
# else: 
#   print("We don't make that")