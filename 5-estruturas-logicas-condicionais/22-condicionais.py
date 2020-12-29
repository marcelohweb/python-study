"""
Estrutura condicionais
if, else, elif

elif = else if
"""

idade = 6

# Obs. Os parênteses não são necessários
# As chaves não são necessárias
# O Python entende que o bloco se inicia com 4 espaços à frente
if idade < 18:
    print('Menor de idade')
    print(idade)
elif idade >= 60:
    print('Idoso')
else:
    print('Maior de idade')


