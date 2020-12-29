"""

Tuplas são bastante parecidas com listas

Existem basicamente duas diferenças:

1 - São representadas por parênteses
2 - São imutáveis. Isso significa que ao se criar uma tupla ela não muda. TOda operação em uma tupla gera uma nova tupla

"""

tupla1 = (1, 2, 3, 4, 5)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5
print(type(tupla2))

# Cuidado

# Isso não é uma tupla. É um int
tupla3 = (4)
print(type(tupla3))

# Isso é uma tupla
tupla4 = (4,)
print(type(tupla4))

# Isso é uma tupla
tupla4 = 4,
print(type(tupla4))

# Criar tupla com um range
tupla5 = tuple(range(11))
print(tupla5)

# Desempacotamento de tupla

tupla = ('Marcelo', 'Soares')

nome, sobrenome = tupla

print(nome)
print(sobrenome)

tupla = (1, 2, 3, 4, 5)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

tupla3 = tupla1 + tupla2

print(tupla3)

# Verificar se valor está contido em tupla

print(3 in tupla)

# Iterando em tupla

for n in tupla:
    print(n)

# Setando chave e iterando pela tupla

for key, value in enumerate(tupla):
    print(key, value)

# Contando elementos em tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a')

print(tupla.count('a'))

nome = 'Marcelo Soares'
tupla = tuple(nome)
# Imprime ('M', 'a', 'r', 'c', 'e', 'l', 'o', ' ', 'S', 'o', 'a', 'r', 'e', 's') porque string é iterável
print(tupla)

meses = 'Janeiro', 'Feveriro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
print(meses[10])

# Iterar com while

i = 0
while i < len(meses):
    print(meses[i])
    i += 1

# Verificar índice de elemento
print(meses.index('Outubro'))

# Slicing - semelhante à lista

# tupla[inicio:fim:passo]

# Por que utilizar tuplas?

# - Tuplas são mais rápidas do que listas
# - Tuplas deixam seu código mais seguro* imutabilidade

