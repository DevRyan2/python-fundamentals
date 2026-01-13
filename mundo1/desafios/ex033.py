a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

maior = a
menor = a

if b > maior:
    maior = b


if b < menor:
    menor = b


if c > maior:
    maior = c

if c < menor:
    menor = c

print(f'Maior: {maior}')
print(f'Menor {menor}')

