teste = str(input('Digite alguma coisa: '))

# cores

fverm_lbran = '\033[0;41m'
fazul_lamare_s = "\033[4;33;44m"
famare_lrox_n = "\033[1;35;43m"
fverd_lbran = "\033[42m"
fpret_lbran = "\033[40m"
fbran_lpret = "\033[7m"

reset = "\033[m"

print(f"{fverm_lbran}Fundo vermelho com letra branca{reset}")

print(f"{fazul_lamare_s}Fundo azul com letra amarela sublinhada{reset}")

print(f"{famare_lrox_n}Fundo amarelo com letra roxa em negrito{reset}")

print(f"{fverd_lbran}Fundo verde com letra branca{reset}")

print(f"{fpret_lbran}Fundo preto com letra branca{reset}")

print(f"{fbran_lpret}Fundo branco com letra preta{reset}")


a = 5
b = 7
print(f'Seus valores sao \033[1;31m{a}\033[m e \033[1;34m{b}\033[m')


print(f"{fverm_lbran}{teste}{reset}")

print(f"{fazul_lamare_s}{teste}{reset}")

print(f"{famare_lrox_n}{teste}{reset}")

print(f"{fverd_lbran}{teste}{reset}")

print(f"{fpret_lbran}{teste}{reset}")

print(f"{fbran_lpret}{teste}{reset}")



cores = {'limpa':'\003[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7m'
}
