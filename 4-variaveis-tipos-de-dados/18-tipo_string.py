"""
Tipo string

Em Python, um dado é considerado do tipo string sempre que estiver entre aspas simples ou aspas duplas.

Ex:

'uma string', '234', 'a', 'True', '42.3'
"uma string", "234", "a", "True", "42.3"

Ou ainda, estiver entre aspas simples triplas

Ex:

'''uma string''', '''234'''

Ou ianda, estiver entre três aspas duplas

Ex:

"""

# """uma string""", """234"""

print(type('Oi')) # <class 'str'> - O mais comum é usar aspas simples

print(type("Oi")) # <class 'str'>

print(type('''Oi''')) # <class 'str'>

print(type("""Oi""")) # <class 'str'>

nome = "Gina's Bar" # Usar aspas duplas quando precisar imprimir aspas simples. O inverso é verdadeiro.

# Ou usar caractere de scape \

nome = 'Gina\'s bar'

print(nome)

print(nome)

nome = 'Marcelo \nSoares'

print(nome)

# Ou

nome = """Marcelo
Soares"""

print(nome)

print(nome[0]) # M

print(nome.upper())

print(nome.lower())

# split

print(nome.split()) # Prints a list ['Marcelo', 'Soares']

print(nome.split()[0]) # Marcelo

nome = 'Geek University'

#Slice de string - from - to
print(nome[0:4]) # Geek

print(nome[5:15]) # Geek

print(nome[::-1]) # Imprime invertido

print(nome.replace('e', '3'))