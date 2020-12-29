"""
Álgebra Booleana, criada por George Boole

2 constantes, Verdadeiro ou Falso

True -> Verdadeiro
False -> Falso

OBS: Sempre com a inicial maiuscula

Errado:

true, false (Em python?)

Certo:

True, False
"""

ativo = False

print(ativo)
print(type(ativo)) # <class 'bool'>

# Operações básicas

# Negação (not)

print(not ativo) # True - porque o valor é False

# Ou (or) - Um ou outro deve ser verdadeiro

logado = True

print(ativo or logado)

# E (and) - Ambos devem ser verdadeiros

print(ativo and logado)