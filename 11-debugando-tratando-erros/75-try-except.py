"""
O bloco try/except -> equivalente ao try catch em java

A forma mais geral e simples é:

try:
    //Trecho de código
except:
    //O que deve ser feito em caso de problema
"""

# Exemplo 1 - Tratando um erro genérico

try:
    geek()
except:
    print('Ocorreu um erro')
finally:
    print('finally block')

try:
    geek()
except NameError as err:  # É possível atribuir um alias ao erro
    print(f'Ocorreu um erro: {err}')
finally:
    print('finally block')

# É possível ter vários blocos except

try:
    geek()
except NameError as err:
    print(f'NameError - Ocorreu um erro: {err}')
except TypeError as err:
    print(f'TypeError - Ocorreu um erro: {err}')
finally:
    print('finally block')


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None


valor = pega_valor({'a': 'valor'}, 'b')
print(valor)


try:
    geek()
except SyntaxError:  # Não vai capturar porque é lançado um NameError
    print('Ocorreu um erro')
finally:
    print('finally block')