n1 = int(input('Digite um número inteiro: '))

print('Escolha uma das bases para conversão:')
print('[ 1 ] para BINÁRIO')
print('[ 2 ] para OCTAL')
print('[ 3 ] para HEXADECIMAL')

escolha = int(input('Sua opção: '))

if escolha == 1:
    binario = bin(n1)
    print(f'O valor {n1} em binario é: {binario[2:]}')


elif escolha == 2:
    octal = oct(n1)
    print(f'O valor {n1} em octal é: {octal[2:]}')


elif escolha == 3:
    hexa = hex(n1)
    print(f'O valor {n1} em hexadecimal é: {hexa[2:]}')


else:
    print(f'O valor digitado é invalido!')


