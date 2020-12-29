"""
Módulo Collections - Deque

Podemos dizer que o deque é uma lista de alta performance
"""

from collections import deque

deq = deque('geek')

print(deq)

deq = deque(['a', 'b', 'c'])

print(deq)

deq.append('d')

print(deq)

deq2 = deque('-');

deq2.extend(deq)

print(deq2)

# Há várias funções que já vimos em listas

print(deq.pop())

print(deq)
