"""
Built-in - Funções "nativas" do python

Em Python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

Onde:

def -> Utilizamos essa palavra reservada para informar ao Python que estamos definindo uma função
nome_da_funcao -> SEMPRE com letras minúsculas e se for nome composto, separado por underlines (Snake Case).
                    Deve ser seguido de dois pontos (:)
parametros_de_entrada -> São opcionais. Em caso de mais de um, devem ser separados por vírgula, sendo opcionais ou não
bloco_da_funcao -> Também chamado de corpo da função ou implementação. Pode ter ou não retorno

"""


def say_hello():
    print('Hello')


say_hello()

# Em python podemos atribuir uma função a uma variável e executá-la chamando a variável. Ex:

# Obs. Sem parênteses
say = say_hello

say()



