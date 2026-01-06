from math import radians, sin, cos, tan

angulo = float(input('Digite um ângulo em graus: '))

radianos = radians(angulo)
seno = sin(radianos)
cosseno = cos(radianos)
tangente = tan(radianos)

print(f'O angulo digitado foi: {angulo:.2f}°')
print(f'Seno: {seno:.2f}')
print(f'Cosseno: {cosseno:.2f}')
print(f'Tangente: {tangente:.2f}')
