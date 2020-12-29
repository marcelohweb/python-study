"""
Loop while

Também serve para iterar sobre sequências

Obs. No Python não existe o do while
"""

i = 0

while i < 10:
    print(i)
    i += 1
    if i == 5:
        break

resposta = ''

while resposta != 'sim':
    resposta = input('Já acabou?')
