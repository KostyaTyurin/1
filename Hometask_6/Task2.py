def args_print_decor(func):
    def decorator(*args):
        func(*args)
        print(*args)
    return decorator

@args_print_decor
def sum(*args):
    res = 0
    for j in args:
        res += j
    print(res)

sum(5, 3, 2, 1)
