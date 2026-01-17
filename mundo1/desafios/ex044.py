print('=' * 10 ,'LOJAS SOUZA', '=' * 10)

preco = float(input('Preço das compras: R$'))

print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')

escolha = int(input('Qual é a opção? '))


if escolha == 1:

    desconto = preco - (preco * 0.10)

    print(f'Sua compra de R${preco:.2f} vai custar R${desconto:.2f} no final.')


elif escolha == 2:

    desconto = preco - (preco * 0.05)

    print(f'Sua compra de R${preco:.2f} vai custar R$ {desconto:.2f} no final.')


elif escolha == 3:

    parcelado = (preco / 2)

    print(f'Sua compra será parcelada em 2x de R${parcelado:.2f} SEM JUROS')


elif escolha == 4:

    parcelas = int(input('Quantas parcelas? '))
    total = preco + (preco * 0.20)
    parcelado = (total / parcelas)

    print(f'Sua compra será parcelada em {parcelas}x de R${parcelado:.2f} COM JUROS')
    print(f'Sua compra de {preco} vai custar {total:.2f} no final.')


