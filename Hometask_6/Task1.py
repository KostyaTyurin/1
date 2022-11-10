def foo(a,b):
    print(a/b)


def decorator_foo(func):
    def decorator(a, b):
        a, b = b, a
        func(a, b)
    return decorator


foo(5,4)
foo = decorator_foo(foo)
foo(4,5)
