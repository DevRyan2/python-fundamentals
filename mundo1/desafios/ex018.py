from math import radians, sin, cos, tan

angulo = float(input('Digite o ângulo que você deseja: '))

radianos = radians(angulo)
seno = sin(radianos)
cosseno = cos(radianos)
tangente = tan(radianos)

print(f'O ângulo de {angulo} tem o SENO de {seno:.2f}')
print(f'O ângulo de {angulo} tem o COSSENO de {cosseno:.2f}')
print(f'O ângulo de {angulo} tem a TANGENTE de {tangente:.2f}')


"""an = float(input('Digite o ângulo que você deseja: '))

seno = sin(radians(an))
cosseno = cos(radians(an))
tangente = tan(radians(an))

print(f'O ângulo de {an} tem o SENO de {seno:.2f}')
print(f'O ângulo de {an} tem o COSSENO de {cosseno:.2f}')
print(f'O ângulo de {an} tem a TANGENTE de {tangente:.2f}')

"""
