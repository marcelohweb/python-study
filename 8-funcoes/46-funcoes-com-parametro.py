def quadrado(numero):
    return numero * numero


# Prints 4
print(quadrado(2))

# Exibe um TypeError
# ret = quadrado(2, 3)
# ret = quadrado()


def soma(valor1, valor2):
    return valor1 + valor2


print(soma(2, 3))


def nome_completo(nome, sobrenome):
    return nome + ' ' + sobrenome


print(nome_completo('Marcelo', 'Soares'))

# Para que a ordem seja ignorada, basta passar os argumentos indicando o nome do parâmetro
print(nome_completo(sobrenome='Soares', nome='Marcelo'))
