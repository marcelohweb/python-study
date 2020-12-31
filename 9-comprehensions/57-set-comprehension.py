ret = {num for num in range(0, 10)}

print(type(ret))
print(ret)

ret = {num * 2 for num in range(0, 10)}

print(ret)

# Gerando um dicionário

ret = {num: num * 2 for num in range(0, 10)}

print(type(ret))
print(ret)

