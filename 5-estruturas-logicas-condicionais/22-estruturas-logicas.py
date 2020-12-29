"""
Estruturas lógicas: and (e), or (ou), not (não), is (é)

Operadores unários
    - not
Operadores binários
    - and, or, is

Usamos o is para comparar se um primeiro valor é o segundo

"""

ativo = True
logado = False

if ativo and logado:
    print('Bem vindo')
else:
    print('Você precisa estar ativo e logado')

if ativo or logado:
    print('Bem vindo')
else:
    print('Você precisa estar ativo e logado')

if not ativo:
    print('Usuário inativo')

if ativo is True:
    print('Usuário Ativo')

if ativo:
    print('Usuário Ativo')