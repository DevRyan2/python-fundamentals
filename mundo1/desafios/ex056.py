soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nomevelho = ''
total_mulher20 = 0


for p in range(1, 5):

    print(f"------{p}ª PESSOA------")
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()

    soma_idade += idade
    media_idade = (soma_idade / 4)

    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nomevelho = nome


    if sexo in 'Mm' and idade > maior_idade_homem:
        nomevelho = nome


    if sexo in 'Ff' and idade < 20:

        total_mulher20 += 1

print(f'A media de idade do grupo é de {media_idade} anos')
print(f'O homem mais velho tem {maior_idade_homem} e se chama {nomevelho}')
print(f'Ao todo são {total_mulher20} com menos de 20 anos')
