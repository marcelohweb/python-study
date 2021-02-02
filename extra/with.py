class MyClass:

    def __init__(self):
        print('Método __init__')

    def __enter__(self):
        print('Método __enter__')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Método __exit__')


myClass = MyClass()

with myClass:
    print('hi')
