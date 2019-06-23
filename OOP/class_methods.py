class User:
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are currrently {cls.active_users} active users"

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(',')
        return cls(first, last, int(age))

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

print(User.display_active_users())
