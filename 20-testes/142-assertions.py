"""
Com TDD, temos os seguintes estágios de desenvolvimento
- Você escreve primeiro o seu teste
- Escreve o código mínimo suficiente para fazer o teste passar (ou seja, executar com sucesso)
- Refatora o código para realizar a funcionalidade e testa novamente
- Uma vez que o teste passe, o recurso é considerado completo

Estes estágios de desenvolvimento do TDD são quase um mantra que os desenvolvedores seguem, conhecidos como:

- Red
- Green
- Refactor

Assertions (Afirmações, checagens, questionamentos)

Se a expressão que queremos testar for verdadeira, retorna None e segue com a execução.
Caso seja falsa levanta um erro do tipo AssertionError

Obs. A palavra 'assert' pode ser utilizada em qualquer função ou código nosso...
Não precisa ser exclusivamente nos testes

"""


# A frase depois da vírgula é exibida em caso de AssertionError
def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos números precisam ser positivos'
    return a + b


soma_numeros_positivos(2, 2)


def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'hamburguer'
    ], 'A comida precisa ser fast-food'


comer_fast_food('pizza')

# Utilizar python -O meu_arquivo.py para ignorar AssertionError
