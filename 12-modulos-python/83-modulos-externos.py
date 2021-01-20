"""
Utilizamos o gerenciador de paotes chamado Pip -> Python Installer Package

Para conhecer todos os pacotes externos oficiais:

https://pypi.org

Utilizando o pacote colorama

from colorama import init
from colorama import Fore, Back, Style

init()

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

"""

import pydf

pdf = pydf.generate_pdf('<h1>this is html</h1>')
with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
