"""
Entendendo o *args

O *args é um parâmetro como outro qualquer. Isso significa que podemos chamar de qualquer coisa, desde que
comece com asteristo

Por convenção, a comunidade decidiu adotar o nome * args para defini-lo

Mas o que é o *args?

O parâmetro *args utilizado em uma função coloca os argumentos passados em uma tupla.
"""

# Ex:


def soma_todos_numeros(*args):
    print(args)
    return sum(args)


soma_todos_numeros()
soma_todos_numeros(1, 2, 3)
soma_todos_numeros(1, 2, 3, 4, 5)

print(soma_todos_numeros(1, 2, 3, 4, 5))

# É possível ter um parâmetro e o *args. O *args não é obrigatório


def soma_compra_cliente(nome_cliente, *args):
    print(nome_cliente)
    return sum(args)


print(soma_compra_cliente('Marcelo', 1, 2, 3))

# É possível

numeros = [1, 2, 3, 4, 5]

# O asterisco força o desempacotamento da lista dentro da função

print(soma_compra_cliente('Marcelo', *numeros))
