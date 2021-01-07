"""
raise -> lança exceptions

raise ValueError('Valor incorreto')

Obs. Nada após o raise é executado
"""

# Exemplo real


def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Oi', 'azul')  # Correto

colore(1, 'azul')  # Error

