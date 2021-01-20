"""
Módulo -> É apenas um arquivo Python que pode ter diversas funções/variáveis para utilizarmos

Pacote -> É um diretório contendo uma coleção de módulos

Obs. Nas versões 2.x do Python, um pacote Python deveria conter um arquivo __init__.py por mais que estivesse vazio

Nas versões 3.x do Python, não é mais obrigatório a utilização deste arquivo, mas normalmente ainda
é utilizado para manter compatibilidade
"""

from meu_pacote import modulo1, modulo2
# Para importar apenas função
# from meu_pacote.modulo1 import get_global1_value

from meu_pacote.meu_sub_pacote import modulo3, modulo4

print(modulo1.get_global1_value('a'))

print(modulo1.pi)

print(modulo2.curso)

print(modulo2.funcao2())

print(modulo3.funcao3())

print(modulo4.funcao4())
