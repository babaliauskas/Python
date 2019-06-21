class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def full_name(self):
        return f'{self.first} {self.last}'

    def initials(self):
        return f'{self.first[0]}.{self.last[0]}'

    def likes(self, thing):
        return f'{self.first} likes {thing}'


user1 = User('Joe', 'Smith', 45)
user2 = User('Blanca', 'Lopez', 34)

print(user1.full_name())
print(user1.initials())
print(user1.likes('Ice Cream'))


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
