"""
Entendendo Iterators e Iterables

Iterator ->
    - Um objeto que pode ter iterado.
    - Um objeto que retorna um dado, sendo um elemento por vez qunando uma função next() é chamada.

Iterable ->
    - Um objeto que irá retornar um iterator quando a funçao iter() for chamada.
"""

nome = 'Hello'  # É iterable mas não iterator
numeros = [1, 2, 3, 4, 5, 6]  # É iterable mas não iterator

# Por baixo dos panos, o python vai pegar o nome e aplicar a função iter()
for letra in nome:
    print(letra)

# print(next(nome))  # TypeError: 'str' object is not an iterator
# print(next(numeros))  # TypeError: 'list' object is not an iterator

# Podemos transformar em iterables

it1 = iter(nome)

print(next(it1))  # Prints H
print(next(it1))  # Prints e
print(next(it1))  # Prints l
print(next(it1))  # Prints l
print(next(it1))  # Prints o

it2 = iter(numeros)

print(next(it2))  # Prints 1
print(next(it2))  # Prints 2
print(next(it2))  # Prints 3
print(next(it2))  # Prints 4
print(next(it2))  # Prints 5
print(next(it2))  # Prints 6

