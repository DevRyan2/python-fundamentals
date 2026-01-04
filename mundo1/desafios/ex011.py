largura = float(input("Largura da parede: "))
altura = float(input('Altura da parede: '))


area = (altura * largura)
tinta = (area / 2)

print(f'Sua parede tem a dimensão de {largura:.2f}x{altura:.2f} e sua área é de {area:.3f}m².')
print(f'Para pintar a essa parede, você precisará de {tinta:.2f}l de tinta.')
