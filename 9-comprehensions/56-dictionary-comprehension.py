"""
Syntax do Dictionary Comprehension

{chave: valor for valor in iterável}
"""

# Ex:

dic = {'a': 1, 'b': 2, 'c': 3}

ret = {chave: valor ** 2 for chave, valor in dic.items()}

print(ret)

# Outro exemplo

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

# Exemplo com lógica condicional

res = {num: ('par' if num % 2 == 0 else 'impar') for num in valores}
print(res)
