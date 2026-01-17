nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))

media = (nota1 + nota2) / 2

print(f'Tirando {nota1:.2f} e {nota2:.2f}, a média do aluno é {media:.1f}')

if media <= 4.9:
    print(f'O aluno está REPROVADO!')


elif media <= 6.9:
    print(f'O aluno está de RECUPERAÇÃO.')


else:
    print(f'O aluno está APROVADO.')


