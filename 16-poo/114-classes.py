"""
É possível ter várias classes em um único arquivo
"""


# Camelcase pattern
class ContaCorrente:
    pass


banco = ContaCorrente()


class Produto:
    pass


produto = Produto()

print(produto)


# Obs. int é uma classe. Classes internas do puthon tem inicial minúscula
inteiro = int(2)

print(type(inteiro))
