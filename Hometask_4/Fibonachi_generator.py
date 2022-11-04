def fibonachi_range(n):
    res = 0
    while res != n:
        yield fibonachi(res)
        res += 1



def fibonachi(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < 0:
        raise ValueError
    else:
        return fibonachi(n-1) + fibonachi(n-2)

for j in fibonachi_range(10):
    print(j)
