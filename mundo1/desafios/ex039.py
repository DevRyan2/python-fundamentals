from datetime import date

ano = int(input('Ano de nascimento: '))
ano_atual = date.today().year

idade = (ano_atual - ano)

print(f'Quem nasceu em {ano} tem {idade} em {ano_atual}.')

if idade <= 16:
    falta = (17 - idade)
    print(f'Você tem {idade} anos, ainda faltam {falta} anos para se alistar.')
    print(f'Seu alistamento será em {falta + ano_atual}.')


elif idade == 17:
    print(f'Você tem {idade} anos, está na hora de se alistar.')


elif idade == 18:
    print(f'Você tem {idade} anos, está no prazo de alistamento.')
else:

    passou = (idade - 18)
    print(f'Já passou {passou} anos do prazo.')
    print(f"Seu alistamento foi em {ano_atual - passou}")
