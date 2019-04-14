from random import randint
player = input(' rock (r), paper (p), or scissors (s)?')

chosen = randint(1,3)
if chosen == 1:
    computer = 'r'
elif chosen == 2:
    computer = 'p'
else:
    computer = 's'

print(player, 'vs', computer)
print('Computer Chose:', computer)

# Draw Case
if player == computer:
    print('DRAW!')

#Player choosing Rock cases:
elif player == 'r' and computer == 'p':
    print('Computer Won!')
elif player == 'r' and computer == 's':
    print('You Won!')

#Player choosing Paper cases:
elif player == 'p' and computer == 'r':
    print('You Won!')
elif player == 'p' and computer == 's':
    print('Computer Won!')

#Player choosing Scissors cases:
elif player == 's' and computer == 'r':
    print('Computer Won!')
elif player == 's' and computer == 'p':
    print('You Won!')