from time import sleep
import emoji

print('''
Você quer ver a queima de fogos de artifícios?

[ 1 ] SIM
[ 2 ] NÃO
''')


escolha = int(input('ESCOLHA: '))

if escolha == 1:
    for c in range(10, -1,  -1):

        print(c)
        sleep(1)

    print(
        emoji.emojize(
            "BOMMM!! BUMMM!! BOMMM!! :fireworks::fireworks::fireworks:", language="alias"
        )
    )


elif escolha == 2:
    print('Tudo bem, podemos tentar mais tarde.')


else:
    print('O valor digitado é invalido, deseja tentar novamente?')
