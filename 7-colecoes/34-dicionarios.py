"""
Dicionários são coleções do tipo Chave => Valor
Análogo ao HashMap em Java ou ao array associativo em PHP ou mapping em Solidity

Dicionários são representados por chaves {}

Obs. Tanto chave quanto valor podem ser de qualquer tipo
Obs. Não podemos ter chaves repetidas
"""

# Prints <class 'dict'>
print(type({}))

# Forma 1
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# Forma 2
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')

print(paises)

# Acessando elementos

# Forma 1

print(paises['br'])

# Forma 2 - Recomendada

print(paises.get('br'))

# Retorna None
print(paises.get('ar'))

pais = paises.get('ar')

if pais:
    print('Encontrado')
else:
    print('Não encontrado')

# É possível setar o valor default no get para caso não seja encontrado
print(paises.get('ar', 'Não encontrado'))

# Tamanho do dicionário

print(len(paises))

# Verifica se contém chave
print(paises.__contains__('br'))

# Ou
print('br' in paises)

# Em python, o tipod e dado None representa o tipo sem tipo ou tipo vazio
# O tipo none sempre será false

numeros = None
# Prints <class 'NoneType'>
print(type(numeros))

# Podemos utilizar qualquer tipo como chave ou valor, inclusive listas, dicionários ou tuplas
# TODO Não consegui colocar lista como chave
# Tuplas como chaves

localidades = {
    (35.4654, 45.6554): 'Escritório em São Paulo',
    (45.4124, 65.6554): 'Escritório em São Paulo',
    (12.4654, 98.6554): 'Escritório em São Paulo'
}

print(localidades)
# Prints <class 'dict'>
print(type(localidades))

# Adicionar elementos em dicionários

# Forma 1
paises['ar'] = 'Argentina'
print(paises)

# Forma 2
dicionarioFr = {'fr': 'França'}
paises.update(dicionarioFr)
print(paises)

# Atualizando dados de um formuário

paises['eua'] = 'Estados Unidos da América'
print(paises)

dicionarioFr = {'fr': 'French'}
paises.update(dicionarioFr)
print(paises)

# Remover dados de um dicionário

# Forma 1
paisRemovido = paises.pop('ar')
# Ao remover, o valor é retornado
print(paisRemovido)
print(paises)

# Forma 2
del paises['fr']

print(paises)

# Métodos de dicionários

d = dict(a=1, b=2, c=3)
print(d)

# Limpar o dicionário
d.clear()
print(d)

# Copiando um dicionário para outro

# Deep - Cria uma nova cópia do dicionário
d1 = dict(a=1, b=2, c=3)
d2 = d1.copy()

d2['d'] = 4

print(d1)
print(d2)

# Shallow - Alterações feitas em um reflitirão no outro. Semelhante a um ponteiro
d2 = d1

d2['d'] = 4

print(d1)
print(d2)

# Forma não usual de criação de dicionários

# Cria um dicionário com a sendo chave e b valor
outro = {}.fromkeys('a', 'b')

print(outro)

# Outra forma
# Cria um dicionário com cada item da lista sendo uma chave e empty sendo o valor de todas
usuario = {}.fromkeys(['nome', 'email', 'photo', 'profile'], 'empty')
print(usuario)

# Obs. Isso não gera com um valor específico para cada chave. A lista da direita será o valor de todas as chaves
usuario = {}.fromkeys(['nome', 'email', 'photo', 'profile'], ['Marcelo', 'test@test.com', '123=', 'Profile text'])
print(usuario)

# Como string é iterável, cria um dicionário com a, b, c, d, e sendo chaves e b o valor de todas
outro = {}.fromkeys('abcde', 'b')
print(outro)

# Cria um dicionário com valores de 1 a 10 sendo chaves e valor sendo o valor de todos
outro = {}.fromkeys(range(1, 11), 'valor')
print(outro)
