def decorator_function_with_arguments(arg1, arg2, arg3):
    def wrap(f):
        print("Inside wrap()")
        print("Decorator arguments:", arg1, arg2, arg3)

        def wrapped_function(a1, a2, a3, a4):
            print("Inside wrapped_f()")
            f(a1, a2, a3, a4)
            print("After f(*args)")
        return wrapped_function
    return wrap


@decorator_function_with_arguments("hello", "world", 42)
def say_hello(a1, a2, a3, a4):
    print('sayHello arguments:', a1, a2, a3, a4)


print("After decoration")

print("Preparing to call sayHello()")
say_hello("say", "hello", "argument", "list")
print("after first sayHello() call")
say_hello("a", "different", "set of", "arguments")
print("after second sayHello() call")