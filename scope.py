# #########       GLOBAL        #########################

# total = 0 

# # Wrong
# def increment():
#   total += 1 
#   return total

# increment() # Error!

# # Good
# def increment():
#   global total
#   total += 1 
#   return total 

# increment() # 1 

# ################################################

# name = "Rusty"

# # Good
# def greet():
#   print(name)
# greet() # Rusty

# # Good
# def greet():
#   name = "Rusty Steele"
#   print(name)
# greet() # Rusty Steele

# # Wrong
# def greet():
#   name += " Steele"
#   print(name)
# greet() # Error!


# ##########################################################################

# ############            NONLOCAL        ####################

#  - Lets us modify a parents variables in a child (aka nested) function


# def outer():
#   count = 0 
#   def inner():
#     nonlocal count  #   Not Global. It looks at the parent
#     count += 1 
#     return count
#   return inner()
