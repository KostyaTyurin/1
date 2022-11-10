from functools import *

def Fibonachi(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonachi(n-1) + Fibonachi(n-2)

def timer(func):
    def decorator(x):
        from time import time
        start = time()
        res = func(x)
        end = time()
        print('Время затраченное на работы программы {0} = {1}'.format(func, end - start))
    return decorator


@timer
def Fibonachi_recurs(n):
    val = Fibonachi(n)
    return val


@timer
def Fibonachi_cycle(n):
    n1, n2 = 0, 1
    if n == 0:
        print(0)
    elif n == 1:
        print(1)
    else:
        for _ in range(n-1):
            res = n1+n2
            n1 = n2
            n2 = res

@timer
@lru_cache(maxsize=None)
def Fibonachi_recurs_time(n):
    return Fibonachi(n)


@timer
@lru_cache(maxsize=None)
def Fibonachi_cycle_time(n):
    n1, n2 = 0, 1
    if n == 0:
        print(0)
    elif n == 1:
        print(1)
    else:
        for _ in range(n-1):
            res = n1+n2
            n1 = n2
            n2 = res


if __name__ == '__main__':
    Fibonachi_recurs(25)
    Fibonachi_cycle(25)
    (Fibonachi_recurs_time(25))
    Fibonachi_cycle_time(25)
