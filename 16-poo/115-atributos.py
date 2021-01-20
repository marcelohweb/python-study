"""
Há 3 tipos de atributos

- Atributos de Instância -> Atributos associados às instâncias
- Atributos de Classe -> Atributos estáticos
- Atributos Dinâmicos -> Atributos de instância que podem ser criados em tempo de execução

# Atributos de instância são atributos declarados dentro do método construtor

"""


class Produto:

    # Em Python, declaramos os atributos de instância dentro do método construtor

    def __init__(self, code, name):
        self.code = code
        self.name = name
        self.is_active = True


# Para dizer que um atributo é privado, utlizados __ no início do nome do atributo. Porém isso é só uma convenção
# A linguagem python não vai impedir que façamos acesso a esses atributos

# Classe com atributos privados
class Banco:

    def __init__(self, code, name):
        self.__code = code
        self.__name = name
        self.public_attribute = 'test'

    def get_code(self):
        return self.__code


banco = Banco(1, 'Banco do Brasil')
# print(banco.codigo)  # AttributeError
print(banco._Banco__code)  # Podemos acessar um atributo privado dessa forma. _NomeDaClasse__nomeDoAtributoPrivado. Conhecido como Name Mangling
print(banco.public_attribute)
print(banco.get_code())


# Atributos de Classe -> Entendi que são semelhantes à atributos estáticos
class Produto:

    dolar = 5.67

    def __init__(self, code, name):
        self.code = code
        self.name = name
        # self.dolar = 8.00  # it works
        # Produto.dolar = 8.00 it works


print(Produto.dolar)

p1 = Produto(1, 'PS4')
print(p1.dolar)

p2 = Produto(2, 'Nintendo')
print(p2.dolar)

Produto.dolar = 6.00
p3 = Produto(3, 'Xbox')
print(p3.dolar)

# Também é possivel criar atributos de classe em tempo de execução

Produto.moeda = 'BR'
print(Produto.moeda)

p3.valor = 5000  # Valor foi criado neste ponto
print(p3.valor)
print(p3.moeda)  # Prints BR

p4 = Produto(4, 'Mega Drive')
print(p4.moeda)  # Prints BR

# Imprime um dicionário com os atributos da classe
print(p4.__dict__)

print(p4.__dict__['name'])

# Deletando atributos

del p4.name

print(p4.__dict__)

# Também é possível apagar atributos estáticos

del Produto.moeda

# print(Produto.moeda)  # AttributeError
