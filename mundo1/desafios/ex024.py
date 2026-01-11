"""
cidade = str(input("Em que cidade você nasceu? ")).upper().strip()

print(cidade.startswith('SANTO'))
"""


cidade = str(input('Em que cidade você nasceu? ')).upper().strip()

print(cidade[:5] == 'SANTO')
