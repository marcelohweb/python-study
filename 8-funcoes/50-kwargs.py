"""
Por convenção, chamamos de **kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras em uma tupla, o **kwargs exige
que utilizemos parâmetros nomeados, e transforma esses parâmetros extras em um dicionário
"""

# Exemplo


def cores_favoritas(**kwargs):
    print(type(kwargs))  # Prints <class 'dict'>
    print(kwargs)


cores_favoritas(nome='Marcelo', sobrenome='Soares', função='Software Engineer')


def teste(idade, nome, *args, solteiro=False, **kwargs):
    print(idade)
    print(nome)
    print(args)
    print(solteiro)
    print(kwargs)


teste('18', 'Joao', 1, 2, 3, solteiro=True, param1='Valor1', param2='Valor2')


def soma_numeros(**kwargs):
    return sum(kwargs.values())


dicionario = dict(valor1=1, valor2=2, valor3=3)
print(sum(dicionario.values()))


print(soma_numeros(valor1=1, valor2=2, valor3=3))

# Força o desempacotamento

print(soma_numeros(**dicionario))
