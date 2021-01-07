try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor inesperado')
else:  # Entra aqui se não entrar no except
    print(f'Você digitou {num}')
finally:
    print('finally block')  # É executado independente de entrar no except ou no else

if 'num' in locals():
    print(f'Você digitou {num}')

try:
    geek()
except (NameError, ValueError) as err:  # É possível passar uma tupla
    print(f'Ocorreu um erro: {err}')
