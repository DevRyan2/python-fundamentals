"""nome = str(input('Digite seu nome completo: ')).strip()

nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()
nome_sem_espaco = len(nome.replace(" ", ""))
separar_nome = nome.split()
letras1nome = len(separar_nome[0])


print(f'Seu nome em maiúsculas é {nome_maiusculo}')
print(f'Seu nome em minúsculas é {nome_minusculo}')
print(f'Seu nome tem ao todo {nome_sem_espaco} letras')
print(f'Seu primeiro nome é {separar_nome[0]} e ele tem {letras1nome} letras')"""


nome = str(input('Digite o seu nome completo: ')).strip()

print(f'Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome.replace(' ', ''))} letras')
print(f'Seu primeiro nome é {nome.split()[0]} e ele tem {len(nome.split()[0])} letras')

