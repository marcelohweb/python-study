"""
São métodos que utilizam dunder

__init__()
"""


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    # Este método mágico retorna o que deve ser exibido na representação do objeto
    # Ex: Quando fazemos um print(objeto)
    # Semelhante a __str__
    def __repr__(self):
        return f'{self.titulo}, {self.autor}, {self.paginas}'

    # Valor que é retornado quando chamamos a função len passando o objeto. Ex: len(objeto)
    def __len__(self):
        return self.paginas

    # Método mágico para o del. Ex: del objeto
    def __del__(self):
        print('Um objeto do tipo Livro foi deletado da memória')

    def __add__(self, other):
        return f'{self} - {other}'


livro = Livro('Python', 'Editora Community', 400)

print(livro)

print(len(livro))

print(livro + Livro('Java', 'Editora Community', 400))

del livro

