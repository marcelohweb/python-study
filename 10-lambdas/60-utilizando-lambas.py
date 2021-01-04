"""
Utilizando Lambdas

COnhecidas por Expressões Lambas, ou simplesmente Lambdas, são funções
"""

# A função não tem nome, x é um parâmetro de entrada

lambda x: 3 * x + 1

# Como utilizar? Atribuindo a uma variável
calc = lambda x: 3 * x + 1

print(type(calc))  # Prints <class 'function'>
print(calc(2))

# Podemos ter expressões lambas com múltiplas entradas. Obs. Função strip remover espaços no início e no fim

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('marcelo', 'soares'))

# Lamba sem entrada e retorno

funcao = lambda: 'Como não amar python?'

print(funcao())

# Outro exemplo

autores = ['Marcelo Soares', 'Paulo José', 'João Silva']

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[1].lower())

print(autores)
