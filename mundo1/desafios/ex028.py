from random import randint
from time import sleep
print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=-" * 20)

n1 = int(input('Em que número eu pensei? '))

print('PROCESSANDO...')
sleep(3)

escolha = randint(0, 5)

if n1 == escolha:
    print(f'PARABÉNS, Você conseguiu me vencer!')



else:
    print(f'GANHEI, Eu pensei no número {escolha} e não no {n1}')

