"""

filter() -> serve para filtrar dados de uma determinada coleção

"""

# Biblioteca para trabalhar com dados estaísticos
import statistics

# Dados doletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)

print(media)

# Obs. Assim como a função map(), a filter() recebe dois parâmetros, sendo uma função e um iterável

# Retorna apenas os valores acima da média

res = filter(lambda x: x > media, dados)

print(list(res))

# Obs. Assim como na função map(), após serem utilizados os dados de filter(), eles são excluídos da memória

print(list(res))

# Retornar onde não está vazio

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

res = filter(lambda pais: len(pais) > 0, paises)

print(list(res))

# Exemplo mais complexo

usuarios = [
    {"username": "joao", "tweets": ["O ceu é azul", "Preserve a natureza"]},
    {"username": "maria", "tweets": ["Eu amo o meu gato"]},
    {"username": "paulo", "tweets": []},
    {"username": "ana", "tweets": ["Oi"]},
    {"username": "gabriela", "tweets": []},
]

# print(usuarios)

# Filtrar usuários que não possuem tweets

inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))

print(inativos)

nomes_pequenos = list(filter(lambda usuario: len(usuario['username']) <= 3, usuarios))
print(nomes_pequenos)

