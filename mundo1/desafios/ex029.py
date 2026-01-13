km = float(input('Qual é a velocidade atual do carro? '))

if km > 80.00:
    multa = (km - 80) * 7
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    print(f'Você deve pagar uma multa de R${multa:.2f}')


else:
    print('Tenha um bom dia! Dirija com segurança!')
