class User:
    active_users = 0

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def full_name(self):
        return f'{self.first} {self.last}'

    def initials(self):
        return f'{self.first[0]}.{self.last[0]}'

    def likes(self, thing):
        return f'{self.first} likes {thing}'

    def is_senior(self):
        return self.age >= 65


user1 = User('Joe', 'Smith', 45)
user2 = User('Blanca', 'Lopez', 34)

# print(user1.full_name())
# print(user1.initials())
# print(user1.likes('Ice Cream'))


############################################

# class Person:
#     def __init__(self):
#         self.name = 'Tony'
#         self._secret = 'hi!'  # use for private
#         self.__msg = 'I like turtles!'    # access need to use _Person__msg
#         self.__lol = 'hahahaha'     # access need to use _Person__lol


# p = Person()

# print(p.name)
# print(p._secret)  # ususally never accessing private variable outside
# print(p._Person__msg)


###########################################

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, number):
        self.balance += number
        return self.balance

    def withdraw(self, number):
        self.balance -= number
        return self.balance


#########################################

class Pet:
    allowed = ['cats', 'dogs', 'rat']

    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!")
        self.name = name
        self.species = species


cat = Pet('Blue', 'cat')
tiger = Pet('Oreo', 'tiger')

print(cat)
print(tiger)
