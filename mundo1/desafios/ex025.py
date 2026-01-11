'''nome = str(input("Qual seu nome completo? ")).upper().strip()


if 'SILVA' in nome:
    print(f'Seu nome tem silva? Sim')

else:
    print(f'Seu nome tem silva? Não')
'''

nome = str(input('Qual seu nome completo? ')).upper().strip()

print(f'Tem "Silva" no seu nome? {"SILVA" in nome}')
