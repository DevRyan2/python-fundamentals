from random import randint
from time import sleep

computador = randint(0, 2)

print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')

jogador = int(input('Qual é a sua jogada? '))

itens = (
    'pedra',
    'papel',
    'tesoura'
)

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ!')
sleep(0.5)

print('-=' * 13)
print(f'O computador jogou {(itens[computador])}')
print(f'O jogador jogou {(itens[jogador])}')
print('-=' * 13)


if computador == 0: # computador jogou pedra

    if jogador == 0:
        print('EMPATE')

    elif jogador == 1:
        print('JOGADOR GANHOU')

    elif jogador == 2:
        print('COMPUTADOR VENCE')

    else:
        print("JOGADA INVÁLIDA")


elif computador == 1:  # computador jogou papel

    if jogador == 0:
        print('COMPUTADOR VENCE')

    elif jogador == 1:
        print('EMPATE')

    elif jogador == 2:
        print('JOGADOR GANHOU')

    else:
        print("JOGADA INVÁLIDA")


elif computador == 2:  # computador jogou tesoura

    if jogador == 0:
        print('JOGADOR GANHOU')

    elif jogador == 1:
        print('COMPUTADOR VENCE')

    elif jogador == 2:
        print('EMPATE')

    else:
        print("JOGADA INVÁLIDA")
