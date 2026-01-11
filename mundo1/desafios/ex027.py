nome = str(input('Digite o seu nome completo: ')).strip().lower()

separar = nome.split()

print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {separar[0]}')
print(f'Seu último nome é {separar[len(separar) - 1]}')

