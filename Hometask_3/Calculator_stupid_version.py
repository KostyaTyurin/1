from Hometask_3.Complex_numbers import Complex

print('Добрый день! Это простенький калькулятор, для работы с комплексными числами')
print('Для работы с ним сначала введите выражение ввида a+b')
text=''
while text != 'No':
    text = input("Введите операцию, которую хотели произвести:")
    print('Далее введите поочереди числа в виде x+yi')
    a = input('a = ')
    b = input('b = ')
    if '+' in a:
        x1 = float(a[:a.find('+')])
        y1 = float(a[a.find('+') + 1:-1])
        a = Complex(x=x1, y=y1)
    elif '-' in a:
        x1 = float(a[:a.find('-')])
        y1 = float(a[a.find('-') + 1:-1])
        a = Complex(x=x1, y=y1)
    elif 'i' not in a:
        a = float(a)


    if '+' in b:
        x2 = float(b[:b.find('+')])
        y2 = float(b[b.find('+') + 1:-1])
        b = Complex(x=x2, y=y2)
    elif '-' in b:
        x2 = float(b[:b.find('-')])
        y2 = float(b[b.find('-') + 1:-1])
        b = Complex(x=x2, y=y2)
    elif 'i' not in b:
        b = float(b)


    print(eval(text))
    text = input('Хотите продолжить? Yes/No')
