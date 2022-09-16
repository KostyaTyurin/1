import time
def fibonachi(n):
    start = time.time()
    list_of_results = list(0 for _ in range(n+1))
    list_of_results[0] = 0
    list_of_results[1] = 1
    for j in range(2, n+1):
        list_of_results[j] = list_of_results[j-1] + list_of_results[j-2]
    end = time.time()
    return(list_of_results[n], end - start)

def fibonachi_r(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonachi_r(n-1) + fibonachi_r(n-2)


