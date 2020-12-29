"""
Escopo de variáveis

Dois casos de escopo:

1 - Variáveis globais -> Reconhecidas em todo o programa
2 - Variáveis globais -> Reconhecidas apenas no bloco onde foram declaradas

Para declarar variáveis em python

nome_da_variavel = valor_da_variavel

Obs. Python é uma linguagem de tipagem dinâmica.

Ao declarar uma variável, nós não especificamos o tipo de dado. O tipo é inferido na atribuição do valor
"""

numero = 42 # Exemplo de variável global
print(numero)
print(type(numero))

# print(nao_existe) - error