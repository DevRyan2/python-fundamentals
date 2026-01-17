nome = str(input("Qual é o seu nome? ")).strip()

nome_lower = nome.lower()
nome_title = nome.title()


if nome_lower == 'ryan':
    print(f'Que nome lindo você tem {nome_title}')

elif nome_lower == 'gustavo':
    print(f'Que nome sem graça você tem {nome_title}')


elif nome_lower in ('maria','breno', 'matheus'):

    print(f'Seu nome é bem popular no brasil {nome_title}')

else:
    print(f'Esse é o nome mais sem graça que eu ja vi {nome_title}')

print(f'Tenha um bom dia {nome_title}!')
