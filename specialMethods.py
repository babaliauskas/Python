from copy import copy


class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"Human named {self.first} {self.last} aged {self.age}"

    def __len__(self):
        return self.age

    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first='Newborn', last=self.last, age=0)
        raise TypeError("Can't add!")

    def __mul__(self, other):
        if isinstance(other, int):
            return [copy(self) for i in range(other)]
        raise TypeError("Can't multiply")


j = Human('Jenny', 'Larsen', 47)
k = Human("Kevin", "Jones", 49)

# triplets = j * 3
# triplets[1].first = 'Jessica'
# print(triplets)

triplets = (j + k) * 3
# print(triplets)


###########################################

class GrumpyDict(dict):
    def __repr__(self):
        print("NONE OF YOUR BUSINESS")
        return super().__repr__()

    def __missing__(self, key):
        print(f"YOU WANT {key}? WELL IT AINT HERE!")

    def __setitem__(self, key, value):
        print("YOU WANT TO CHANGE THE DICTIONARY?")
        print("OK FINE...")
        super().__setitem__(key, value)


# data = GrumpyDict({"first": "Tom", "animal": "cat"})
# data['city'] = 'Tokyo'
# print(data)


###########################################

class Train:
    def __init__(self, num):
        self.num = num

    def __repr__(self):
        return f"{self.num} car train"

    def __len__(self):
        return self.num


a_train = Train(4)
print(a_train)
print(len(a_train))
