import random


act = ['rock', 'scissors', 'paper']

player1 = random.choice(act)
player2 = random.choice(act)



if player2 == player1:
    print('Tie! Both players chose the same action.')
    print(player1)
    print(player2)

elif player1 == 'rock' and player2 == 'scissors':
    print(player1)
    print(player2)
    print('player1 won!!!')

elif player1 == 'paper' and player2 == 'rock':
    print(player1)
    print(player2)
    print('player1 won!!!')

elif player1 == 'scissors' and player2 == 'parper':
    print(player1)
    print(player2)
    print('player1 won!!!')

else:
    print(player1)
    print(player2)
    print('player2 won!!!')    