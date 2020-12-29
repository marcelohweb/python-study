"""
Em outras linguagens de programação, quando falamos em conjuntos, estamos falando da Teoria dos Conjuntos da Matemática

Em Python, os conjuntos são chamados de Sets

Aceitam qualquer tipo de dados

Assim, da mesma forma que na matemática:

- Sets não possuem valores duplicados;
- Sets não possuem valores ordenados;
- Elementos não são acessados por índice.

Utilizamos conjuntos quando precisamos armazenar elementos mas não nos importamos com a ordenação deles e
quando não precisamos nos preocupar com chaves e itens duplicados

Os conjuntos são referenciados com chaves {}

Diferença entre conjuntos e dicionários

- Dicionários (mapas) possuem chave e valor
- Conjuntos (sets) só possuem valor
"""

# Defininco um set

# Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 6})
print(type(s))
# Imprime {1, 2, 3, 4, 5, 6} porque sets não possuem valores duplicados
print(s)

# Forma 2

s = {1, 2, 3, 3, 4, 4, 5, 5, 6}
print(type(s))
print(s)

# É possível criar sets a partir de listas ou tuplas

lista = [1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
print(lista)

s = set(lista)
print(s)

# Podemos iterar normalmente em um set
for valor in s:
    print(valor)

# Adicionando elementos em um conjunto
s.add(7)
s.add(8)
s.add(8)

print(s)

# Removendo elementos de um conjunto

# Obs. Não remove pelo índice, e sim por valor. Sets não são indexados
s.remove(1)
print(s)

# Forma 2

s.discard(2)
print(s)

# Deep copy e shallow copy funcionam

# Podemos remover todos os itens de um conjunto

s.clear()

print(s)

# Métodos matemáticos de conjuntos

estudantes_java = {'Marcelo', 'Joao', 'Paulo', 'Pedro'}
estudantes_python = {'Marcelo', 'Marcus', 'Ana', 'Rafael'}

# Union/distinct

# Forma 1

todos = estudantes_java.union(estudantes_python)

print(todos)

# Forma 2

todos = estudantes_java | estudantes_python

print(todos)

# Interseção

# Forma 1

intersecao = estudantes_java.intersection(estudantes_python)

print(intersecao)

# Forma 2

intersecao = estudantes_java & estudantes_python

print(intersecao)

# NOT IN

not_in = estudantes_java.difference(estudantes_python)

print(not_in)

# Outras funções matemáticas

numeros = {1, 2, 3, 4, 5, 6}

print(sum(numeros))
print(max(numeros))
print(min(numeros))
print(len(numeros))




