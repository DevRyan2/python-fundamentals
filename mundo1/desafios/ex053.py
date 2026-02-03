frase = str(input('Digite uma frase: ')).strip().upper()

tirar_espaco = frase.replace(' ',  '')
inverter = tirar_espaco[::-1]

print(f'O inverso de {frase} é {inverter}')

if inverter == tirar_espaco:
    print(f'{inverter} é um palíndromo')


else:
    print(f'{inverter} não é um palíndromo')
