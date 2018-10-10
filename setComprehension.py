first = {x**2 for x in range(10)}
print(first)

second = {x:x**2 for x in range(10)}
print(second)

third = {i for i in 'hello'}
print(third)

string = 'hello'
print({char for char in string if char in 'aeiou' })

string2 = 'hello hahahah'
print({char for char in string2 if char in 'aeiou'})