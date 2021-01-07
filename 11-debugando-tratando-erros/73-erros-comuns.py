"""
Erros mais comuns em Python

* SyntaxError

def funcao:
    print('oi')

* NameError -> Variável ou função não foi definida

printf('oi')

* TypeError -> Quando uma ação é aplicaada ao tipo errado

len(1)

* IndexError -> Quando tentamos acessar um elemento em um índice inválido

lista = ['Oi']
print(lista[1])

* ValueError -> Quando uma função ou operaao built-in (integrada) recebe um argumento com tipo correto mas valor inapropriado

print(int('Geek'))

* KeyError -> Quando tentamos acessar um dicionário com uma chave que não existe

dic = {'a': 'oi'}
print(dic['b'])

* AttributeError -> Ocorre quando uma variável não tem um atributo/função

tupla = (11, 2, 31, 4)
print(tupla.sort())

* IdentationError -> Ocorre quando não respeitamos a identação do Python (4 espaços)

def nova():
print('oi')

"""