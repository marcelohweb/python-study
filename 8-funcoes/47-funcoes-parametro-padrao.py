"""
Funções com parãmetro default (opcional)

Obs. Os parâmetros opcionais devem sempre estar no final

Uma função pode receber qualquer tipo de dado como parâmetro, incluindo outra função
"""


def exponecial(valor, potencia=2):
    return valor ** potencia


print(exponecial(2, 3))
print(exponecial(2))


def minha_funcao(valor1='Valor Default 1', valor2='Valor Default 2'):
    return f'valor1: {valor1}, valor2: {valor2}'


# Para passar apenas os últimos valores, podemos fazer:
print(minha_funcao(valor2='Alterado'))

# Exemplo de função que recebe outra função como parâmetro


def soma(num1, num2):
    return num1 + num2


def subtrai(num1, num2):
    return num1 - num2


def operacao(num1, num2, func=soma):
    return func(num1, num2)


print(operacao(2, 3, ))
print(operacao(2, 3, subtrai))

# Escopo

# É possível acessar uma variável global dentro de uma funçãomas não é possível alterá-la dentro da função.
# Na verdade a alteração só será vista dentro do escopo da função e não dentro do escopo global
variavel_global = 'Geek'


def diz_oi():
    variavel_global = 'alterado'  # Aqui ela é local
    outra_variavel_local = 'Valor local'
    return f'Oi {variavel_global}'


print(diz_oi())
# NameError: name 'outra_variavel_local' is not defined
# print(outra_variavel_local)

total = 0


def incrementa():
    global total  # Diz que é uma variável global
    total += 1


print(total)  # Prints 0
incrementa()
print(total)  # Prints 1
incrementa()
print(total)  # Prints 2

# Podemos ter funções declaradas dentro de funções


def fora():
    contador = 0

    def dentro():
        nonlocal contador  # Diz que esta variável está em uma função anterior
        contador += 1
        return contador
    return dentro()


print(fora())  # Prints 1
