casa = float(input("Valor da casa: R$"))
salario = float(input("Salário do comprador: R$"))
anos = int(input("Quantos anos de financiamento? "))


meses = (anos * 12)
prestacao = (casa / meses)
limite = (salario * 0.30)

print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos.')
print(f'A prestação será de R${prestacao:.2f}')

if prestacao <= limite:
    print(f'Financiamento APROVADO')


else:
    print('Financiamento NEGADO')
