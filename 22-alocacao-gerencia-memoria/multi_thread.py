"""
Obs. O tempo de execução com multi threads foi maior que com single thread.

No pyton, apenas uma sequência de bytecode na VM de Python é executado por vêz.

Isso ocorre devido ao GIL - Python Global Interpreter Lock.

GIL é um mutex -> Exclusão mutua -> Técnica usada em programação concorrente para evitar que dois processos
tenham acesso simultaneamente a um recurso compartilhado.

Em resumo, o GIL é necessário porque o gerenciamento de memória do CPython não é thread-safe.

O GIL evita que programas CPython multithread tirem proveito total de multiprocessadores em certas situações.

Algumas coisas como blocking or long-running operations, such as I/O, image processing, and NumPy number crunching,
funcionam fora do Gil.

Uma alternativa é utilizar multiprocessing para que cada processo tenha o seu interpretador python e espaço de memória.
Assim o GIL não será um problema.

"""

import time
from threading import Thread

contador = 50000000


def contagem_regressiva(n):
    while n > 0:
        n -= 1


t1 = Thread(target=contagem_regressiva, args=(contador//2,))
t2 = Thread(target=contagem_regressiva, args=(contador//2,))

inicio = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
fim = time.time()

print(f'Tempo sem segundos: {fim - inicio}')

# Tempo sem segundos: 3.1512093544006348
