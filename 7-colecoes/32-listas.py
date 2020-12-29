"""
Listas em Python funcionam como vetores/arrays/matrizes, com a diferença de serem DINÂMICOS e de podermos
colocar QUALQUER tipo de dado.

- Dinâmico: Não possui tamanho fixo

As listas em Python são representadas por colchetes []
"""

print(type([]))

lista1 = [1, 5, 7, 8, 11, 15, 20]

lista2 = ['M', 'a', 'r', 'c', 'e', 'l', 'o']

for letra in lista2:
    print(letra)

lista3 = list(range(11))

print(lista3)

lista4 = list('Marcelo Soares')

# prints ['M', 'a', 'r', 'c', 'e', 'l', 'o', ' ', 'S', 'o', 'a', 'r', 'e', 's']
print(lista4)

# chegar se valor está contido em lista
find = 'M'

if find in lista4:
    print(f'lista4 contém {find}')

lista4.sort()

# O método count retorna a quantidade de ocorrências de um determinado elemento
print(lista4.count('a'))

"""
Adicionar elementos em listas
"""

lista4.append('X')

print(lista4)

# Adiciona a lista dentro da lista, não os elementos apenas
lista4.append(['S', 'o', 'a', 'r', 'e', 's'])

print(lista4)

# Adiciona os elementos dentro da lista
lista4.extend(['S', 'o', 'a', 'r', 'e', 's'])

print(lista4)

# Adiciona as letras separadamente porque string é iterável
lista4.extend('Soares')

print(lista4)

# Insere um novo valor em um índice específico da lista. O valor que estava nessa posição será deslocado para a direita
lista4.insert(2, 'Novo Valor')

print(lista4)

# É possível juntar duas listas

lista1 = ['a', 'b', 'c']

lista2 = ['c', 'd', 'e']

# Mesmo que lista1.extend(lista2)
lista3 = lista1 + lista2

print(lista3)

# Inverte a lista
# Mesmo que lista3[::-1]
lista3.reverse()

print(lista3)

# Copiar uma lista. No final do arquivo é explicada a diferença de deep copy e c copy
lista4 = lista3.copy()

print(lista4)

# Tamanho da lista
print(len(lista4))

# Remover o último elemento de uma lista
# O pop não só remove o último elemento mas também retorna
print(lista4.pop())

print(lista4)

# Remover de índice específico
# Os elementos à direita serão deslocados para a esquerda
print(lista4.pop(1))

print(lista4)

# Limpar lista

lista4.clear()

print(lista4)

# Repetir os elementos da lista
lista = [1, 2, 3]

nova = lista * 3;

# prints [1, 2, 3, 1, 2, 3, 1, 2, 3]
print(nova)

# Converter string em lista

# Ex 1:

nome = 'Marcelo Soares'
nome = nome.split()
# Prints ['Marcelo', 'Soares']. Por padrão, o split separa os elementos por espaço
print(nome)

valor = 'Texto-separado-por-hífen'
valor = valor.split('-')
# Prints ['Texto', 'separado', 'por', 'hífen']
print(valor)

# Fazendo o caminho reverso
valor = '-'.join(valor)

print(valor)

lista1 = ['a', 'b', 'c']

# Iterando em lista

# Exemplo 1
for valor in lista1:
    print(valor)

# Exemplo 2
indice = 0
while indice < len(lista1):
    print(lista1[indice])
    indice += 1

# Gerando chaves e valores ao iterar na lista
for key, value in enumerate(lista1):
    print(key, value)

lista1 = list(enumerate(lista1))
# Prints [(0, 'a'), (1, 'b'), (2, 'c')]
print(lista1)

# Acessando valores por índices reversos
# Imprime o último elemento da lista e assim por diante
print(lista1[-1])

lista1 = ['a', 'b', 'c', 'd', 'c']

# Encontrar o índice de um elemento na lista
# Prints 2. Caso o elemento não exista na lista, será exibido um ValueError
# Se tiver mais de uma ocorrência na lsita, retorna o índice do primeiro elemento encontrado
print(lista1.index('c'))

# É possível especificar um índice para iniciar a busca a partir dele
# Ex: Comece a buscar a partir do índice 3. Neste caso, irá imprimir 4
print(lista1.index('c', 3))

# Também é possível especificar um índice fim
# Ex: Busque do índice 3 ao 5
print(lista1.index('c', 3, 5))

# Slice em listas
# Lista[inicio:fim:passo]
# Do índice 1 ao final
print(lista1[1:])

# Toda a lista
print(lista1[::])

# Do início ao índice 2. O último índice não é inclusivo. Imprime o índice 0 e o índice 1
print(lista1[:2])

# Toda a lista com um passo de 2 em 2
print(lista1[::2])

# Invertendo valores de uma lista
nomes = ['Marcelo', 'Soares']
# Os dois primeiros índices recebem os reversos
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

# Ou

nomes.reverse()

print(nomes)

# Funções importantes

listaNum = [1, 2, 3, 4, 5, 6]

print(sum(listaNum))
print(max(listaNum))
print(min(listaNum))
print(len(listaNum))

# Transformar lista em tupla

tupla = tuple(listaNum)
print(tupla)

# Desempacotamento de lista

listaNum = [1, 2, 3]

# Obs. Deve haver a mesma quantidade de variáveis e valores da lista
num1, num2, num3 = listaNum

print(num1)
print(num2)
print(num3)

# Copiando uma lista para outra (Shallow Copy e Deep Copy)

lista1 = [1, 2, 3]

# Deep Copy

lista2 = lista1.copy()

lista2.append(4)

# O que faz em uma não afeta na outra. São duas listas diferentes - Deep Copy

# [1, 2, 3]
print(lista1)
# [1, 2, 3, 4]
print(lista2)

# Shallow copy

lista2 = lista1
lista2.append(4)

# [1, 2, 3, 4]
print(lista1)
# [1, 2, 3, 4]
print(lista2)

carrinho = []
produto = ''

while produto != 'sair':
    produto = input('Informe um produto: ')
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)
