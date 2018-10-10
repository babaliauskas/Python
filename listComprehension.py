

# num = [1,2,3,4,5]
# nums2 = [x*10 for x in num]
# # print(nums2)

# name = 'colt'
# name2 = [char.upper() for char in name]
# # print(name2)

# friends = ['lukas', 'mode', 'siga']
# friends2 = [friend[0].upper() for friend in friends]
# # print(friends2)


# numbers = [1,2,3,4,5,6,7,8]
# evens = [num for num in numbers if num % 2 == 0]
# odds = [num for num in numbers if num % 2 != 0]
# print(evens)
# print(odds)

# numbers2 = [num*2 if num % 2 == 0 else num/2 for num in numbers]
# print(numbers2)

# vowels = 'This is so much fun!'
# vowels2 = ''.join(char for char in vowels if char not in 'aeiou')
# print(vowels2)

# names = ['Elie', 'Tim', 'Matt']
# answer2 = [val[::-1].lower() for val in names]
# print(answer2)

# num1 = [1,2,3,4,6]
# num2 = [3,4,5,6]
# answer = [val for val in num1 if val in num2]
# print(answer)


# board = [[num for num in range(1,4)] for val in range(1,4)]
# print(board)

# board2 = [['X' if num % 2 != 0 else 'O' for num in range(1,4)] for val in range(1,4)]
# print(board2)