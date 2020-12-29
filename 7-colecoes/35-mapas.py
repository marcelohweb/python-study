"""
Mapas -> Conhecidos em Python como Dicionários
"""

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# Iterando sobre dicionários

for chave in paises:
    print(chave)
    print(paises[chave])
    print(f'{chave}: {paises[chave]}')

print(paises.keys())

print(paises.values())

for valor in paises.values():
    print(valor)

# Desempacotamento de dicionários

# Iterar por chaves e valores

for chave, valor in paises.items():
    print(f'chave: {chave} -  valor: {valor}')

# Algumas funções como sum, max e min também funcionam com dicionários se todos os valores forem inteiros

faturamento = {'jan': 100, 'fev': 150, 'mar': 200}

print(sum(faturamento.values()))
print(max(faturamento.values()))
print(min(faturamento.values()))
print(len(faturamento))

