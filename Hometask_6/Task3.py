def error_message_decor(func):
    def decorator(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception:
            print('error')
    return decorator

@error_message_decor
def sum(*args):
    res = 0
    for j in args:
        res += j
    print(res)


sum(1,2, 'fjvb')
