from random import choice


nome1 = input('Nome do primeiro aluno: ')
nome2 = input('nome do segundo aluno: ')
nome3 = input('Nome do terceiro aluno: ')
nome4 = input('Nome do quarto aluno: ')

nomes = [nome1, nome2, nome3, nome4]

escolha = choice(nomes)

print(f'O aluno escolhido foi: "{escolha}"')
