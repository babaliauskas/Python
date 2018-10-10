import secrets

player_score = 0
computer_score = 0
while player_score < 3 and computer_score < 3: 
  print("..paper..")
  print("..rock..")
  print("..scissors..")
  print(f'Player score: {player_score}')
  print(f'Computer Score: {computer_score}')
  player1 = input().lower()
  computer = ['rock', 'paper', 'scissors']
  cpu = secrets.choice(computer)

  if player1 == 'quit' or player1 == 'q':
    break

  if player1 == cpu:
    print('Draw!')
  elif player1 == 'paper':
    if cpu == 'rock':
      print('player 1 wins!')
      player_score += 1
    else:
      print('cpu wins!')
      computer_score += 1
  elif player1 == 'rock':
    if cpu == 'scissors':
      print('player 1 wins!')
      player_score += 1
    else:
      print('cpu wins!')
      computer_score += 1
  elif player1 == 'scissors':
    if cpu == 'paper':
      print('player 1 wins!')
      player_score += 1
    else:
      print('cpu wins!')
      computer_score += 1
  else: 
    print('Please enter a valid move!')


print(f'Player score: {player_score}')
print(f'Computer Score: {computer_score}')
if player_score == 3:
  print('Player wins!')
elif player_score == computer_score:
  print("It's a tie")
else:
  print('Computer wins!')