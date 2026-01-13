distancia = float(input('Qual é a distância da viagem?  '))

print(f'Você está prestes a começar uma viagem de {distancia:.2f}km.')

if distancia <= 200:
    s = distancia * 0.50


else:
    s = distancia * 0.45


print(f"Preço da viagem: R${s:.2f}")
