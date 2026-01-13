'''
nome = str(input('Qual é seu nome? ')).lower().strip()

if nome == 'gustavo':
    print('Que nome lindo você tem!')


else:
    print('Seu nome é tão normal!')

print(f'Bom dia, {nome}!')
'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

print(f'A sua media foi {media:.2f}')


if media >= 6:
    print('Sua média foi boa, PARABÉNS!')

else:
    print('Sua média foi ruim! ESTUDO MAIS.')


#print('PARABÉNS' if media >= 3 else 'ESTUDE MAIS')
