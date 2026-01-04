# raiz quadrada ** (1/2) com dois numeros
# raiz quadrada ** (1/3 ) com tres numeros

nome = input('Digite o seu nome: ')

print(f'Prazer em te conhecer {nome:=^20}!')

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

s = (n1 + n2)
m = (n1 * n2)
d = (n1 / n2)
di = (n1 // n2)
e = (n1 ** n2)

print(f'A soma é {s}, o produto é {m} e a divisão é {d:.2f}.', end=' >>> ')
print(f'Divisão inteira {di} e potência {e}.')
