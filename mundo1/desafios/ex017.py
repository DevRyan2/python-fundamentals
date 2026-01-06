from math import hypot

cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))

hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print(f'A hipotenusa  vai medir {hipotenusa:.2f}')



'''co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)

print(f'A hipotenusa vai medir {hi:.2f}')'''

