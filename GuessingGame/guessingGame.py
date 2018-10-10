import random

random_number = random.randint(1,10)

while True:
  num = input('Pick a number: ')
  num = int(num)
  if num < random_number:
    print('Too low: ')
  elif num > random_number: 
    print('Too high: ')
  else: 
    print('You Won!')
    yes = input('Do you wanna play again? (y/n): ')
    if yes == 'y':
      random_number = random.randint(1,10)
      num = None
    else: 
      print('Thank you for playing!')
      break

