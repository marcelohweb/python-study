x = 10

print(type(x))

y = x

print(type(y))

print(id(x))  # Prints the same id
print(id(y))  # Prints the same id

language = 'python'

print(id(language))

x = 5

print(y)  # Prints 10

#  15 será um objeto na memória, x e y apontarão para 15
x = 15
y = 15

print(id(x))  # Prints the same id
print(id(y))  # Prints the same id
