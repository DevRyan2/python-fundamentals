num = int(input('Digite um número: '))

cores = {

    'blue':'\033[34m',
    'red':'\033[31m',
    'reset':'\033[m'

}


total = 0

for c in range(1, num + 1):

    if num % c == 0:
        print(f'{cores['blue']}', end=' ') # cor azul

        total += 1

    else:
        print(f'{cores["red"]}', end=' ') # cor vermelha

    print(f'{c}{cores["reset"]}', end=" ")

print(f"\nO número {num} foi divisível {total} vezes", end=' ')

if total == 2:
    print('e por isso ele é PRIMO!')


else:
    print('e por isso ele NÃO É PRIMO')
