# ==================== FATIAMENTO (SLICE) ====================
print("=" * 20)
print("FATIAMENTO")
print("=" * 20)

frase = "Curso em Vídeo Python"

# Como acessar partes da string:

print(frase[9])  # Pega 1 caractere na posição 9 → 'V'

print(frase[9:21])  # Pega do 9 ao 20 (final não inclui) → 'Vídeo Python'

print(frase[9:21:2])  # Do 9 ao 20, pulando de 2 em 2 → 'Vdo yhn'

print(frase[:5])  # Do início até posição 4 → 'Curso'

print(frase[15:])  # Da posição 15 até o fim → 'Python'

print(frase[9::3])  # Do 9 até o fim, pulando de 3 em 3 → 'VePh'

print(frase[::2])  # Tudo, pulando de 2 em 2 → 'Croe íe yhn'


# ==================== ANÁLISE ====================

print("=" * 20)
print("ANÁLISE")
print("=" * 20)

print(len(frase))  # Tamanho total → 21 caracteres

print(frase.count("o"))  # Conta quantos 'o' existem → 3

print(frase.count("o", 0, 13))  # Conta 'o' só do 0 ao 12 → 1

print(frase.find("deo"))  # Posição onde começa 'deo' → 11

print(frase.find("Android"))  # Se não existe retorna → -1

print("Curso" in frase)  # Verifica se existe → True

# ==================== TRANSFORMAÇÃO ====================

print("=" * 20)
print("TRANSFORMAÇÃO")
print("=" * 20)

frase2 = "   Aprenda Python  "

print(frase.replace("Python", "Android"))  # Troca Python por Android

print(frase.upper())  # TUDO MAIÚSCULO

print(frase.lower())  # tudo minúsculo

print(frase.capitalize())  # Só primeira letra maiúscula

print(frase.title())  # Primeira De Cada Palavra maiúscula

print(frase2.strip())  # Remove espaços dos lados

print(frase2.rstrip())  # Remove espaços da direita →

print(frase2.lstrip())  # Remove espaços da esquerda


# ==================== DIVISÃO ====================
print("=" * 20)
print("DIVISÃO")
print("=" * 20)

# Divide a string em uma lista, separando pelos espaços

print(frase.split())  # → ['Curso', 'em', 'Vídeo', 'Python']


# ==================== JUNÇÃO ====================

print("=" * 20)
print("JUNÇÃO")
print("=" * 20)

frase_cortada = frase.split()

# Junta lista de volta em string, colocando espaço entre palavras

print(" ".join(frase_cortada))  # → 'Curso em Vídeo Python'
