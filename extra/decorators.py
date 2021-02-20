def my_decorator(name):
    print(name)

    def wrap(processor):
        processor._worker = 'a'
        print(processor('adsadas'))
        print(processor._worker)
        return processor

    return wrap


@my_decorator('aaaaa')
def say_hello(message):
    return message


print(say_hello('hi'))


def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice


@do_twice
def say_whee():
    print("Whee!")


say_whee()


@do_twice
def greet(name):
    print(f"Hello {name}")


greet('Marcelo')


@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


hi_adam = return_greeting("Adam")
print(hi_adam)


def dobra_soma(func):
    print(func)

    def wrap(number1, number2):
        print(f'{number1} + {number2}')
        return 2 * (number1 + number2)
    return wrap


@dobra_soma
def soma(num1, num2):
    return num1 + num2


print(soma(2, 2))
