import random

choices = ['pedra', 'papel', 'tesoura']

computer = random.choice(choices)

player = None
print('O computador escolheu {}'.format(computer))
print('O jogador escolheu {}'.format(player))

while player not in choices:
    player = str(input('Escolha pedra, papel ou tesoura: ')).lower()


if player == computer:
    print('Empate!')
elif player == 'pedra' and computer == 'tesoura':
    print('Você ganhou!')
elif player == 'tesoura' and computer == 'papel':
    print('Você ganhou!')
elif player == 'papel' and computer == 'pedra':
    print('Você ganhou!')
elif player == 'tesoura' and computer == 'pedra':
    print('Você perdeu!')
elif player == 'pedra' and computer == 'papel':
    print('Você perdeu!')
elif player == 'papel' and computer == 'tesoura':
    print('Você perdeu!')
