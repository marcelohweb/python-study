"""
Dunder -> Double under

Dunder Name -> __name__
Dunder Main -> __main__

EM Python, são utilizados dunder para criar funções, atributos/propriedades etc utilizando Double Under
para não gerar conflito com os nomes esses elementos na programação.

Em C temos:

int main() {
    return 0
}

E, Java temos:

public static void main(String[] args) {

}

Em Python, se executarmos um módulo Python diretamente na linha de comando, internamente o Python atribuirá
à variável __name__ o valor __main__ indicando que este módulo é o módulo de execução principal.
"""

#  Prints meu_modulo está sendo importado.
import meu_modulo

print(__name__)  # Prints __main__
