salario = float(input('Qual  é o salário do funcionário? R$'))

if salario > 1250:
    calcule = (salario * 0.10) + salario
    print(f"Quem ganhava R${salario:.2f} passa a ganhar R${calcule:.2f} agora.")

else:
    calcule = (salario * 0.15) + salario
    print(f"Quem ganhava R${salario:.2f} passa a ganhar R${calcule:.2f} agora.")
