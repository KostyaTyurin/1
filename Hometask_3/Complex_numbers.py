import math
import numpy as np


class DiffValueFormsError(Exception):
    def __init__(self, message):
        self._message = message

    def __str__(self):
        return self._message



class Complex:

    def __init__(self, x=None, y=None, r=None, fi=None):
        self.set(x, y, r, fi)
        try:
            if self.storage[0] is not None and self.storage[1] is not None:
                r, fi = self.exp()
            elif self.storage[2] is not None and self.storage[3] is not None:
                x, y = self.alg()
            elif (self.storage[0] is None and self.storage[1] is not None) or (self.storage[0] is not None and  self.storage[1] is None):
                raise DiffValueFormsError('Можно использовать аргументы только одной формы')
            elif (self.storage[2] is None and self.storage[3] is not None) or (self.storage[2] is not None and  self.storage[3] is None):
                raise DiffValueFormsError('Можно использовать аргументы только одной формы')
        except DiffValueFormsError:
            print('Попробуй пересоздать объект класса')
            try:
                text = input('Какую форму числа выберешь - тригонометрическую? : Yes/No')
                if (text != "Yes") and (text != "No"):
                    raise KeyError("Попробуй ввести заново")
            except KeyError:
                print('Кажись ты набрал не тот текст, попробуй еще раз')
                text = input('Какую форму числа выберешь - тригонометрическую? : Yes/No')
            finally:
                if text == 'Yes':
                    r = float(input('r = '))
                    fi = float(input('fi = '))
                    self.set(x=None, y=None, r=r, fi=fi)
                    x, y = self.alg()
                elif text == 'No':
                    x = float(input('x = '))
                    y = float(input('y = '))
                    self.set(x, y, r=None, fi=None)
                    r, fi = self.exp()
                self.storage = {0: x, 1: y, 2: r, 3: fi}
        finally:
            self.storage = {0: x, 1: y, 2: r, 3: fi}

    def set(self, x, y, r, fi):
        self.storage = {0: x, 1: y, 2: r, 3: fi}

    def get_alg(self):
        return self.storage[0], self.storage[1]

    def get_exp(self):
        return self.storage[2], self.storage[3]

    def exp(self):
        x, y = self.get_alg()
        r = math.sqrt(x ** 2 + y ** 2)
        cos_fi = x / r
        fi = math.acos(cos_fi)
        return r, fi

    def alg(self):
        r, fi = self.get_exp()
        a = r*math.cos(fi)
        b = r*math.sin(fi)
        return a, b

    def __add__(self, other):
        x1, y1 = self.get_alg()
        if type(other) is Complex:
            x2, y2 = other.get_alg()
            return Complex(x1+x2, y1+y2)
        else:
            return Complex(x1+other, y1)

    def __radd__(self, other):
        try:
            if type(other) != int or type(other) != float:
                raise TypeError
        except TypeError:
            other = float(input('Попробуй ввести еще один раз : '))
        finally:
            x1, y1 = self.get_alg()
            print(type(x1), y1)
            return Complex(other + x1, y1)

    def __sub__(self, other):
        x1, y1 = self.get_alg()
        x2, y2 = other.get_alg()
        return Complex(x1 - x2, y1 - y2)

    def __rmul__(self, other):
        r, fi = self.get_exp()
        return Complex(r=other*r, fi=fi)

    def __mul__(self, other):
        if type(self) == Complex and type(other) == Complex:
            r1, fi1 = self.get_exp()
            r2, fi2 = other.get_exp()
            return Complex(None, None, r1 * r2, fi1 + fi2)
        elif type(other) != Complex:
            r1, fi1 = self.get_exp()
            return Complex(r=r1*other, fi=fi1)
        elif type(self) != Complex:
            r1, fi1 = other.get_exp()
            return Complex(r=r1 * self, fi=fi1)

    def __truediv__(self, other):
        r1, fi1 = self.get_exp()
        r2, fi2 = other.get_exp()
        try:
            r = r1/r2
            fi = fi1-fi2
        except ZeroDivisionError:
            print('Ты совсем дурачек, на ноль собрался делить...')
            print('А ну-ка пересоздай элемент класса')
            r2 = int(input('Введи длину вектора комплексного числа: '))
            fi2 = int(input('Введи фазу : '))
            other.__setitem__(2, r2)
            other.__setitem__(2, fi2)
        finally:
            return Complex(None, None, r1 / r2, fi1 - fi2)

    def __eq__(self, other):
        self_x, self_y = self.get_exp()
        ins_x, ins_y = other.get_exp()
        if (self_x == ins_x) & (self_y == ins_y):
            return True
        else:
            return False

    def __getitem__(self, item):
        return self.storage[item]

    def __setitem__(self, key, value):
        try:
            if type(value) == int or type(value) == float:
                None
            else:
                raise TypeError('Было веденно что-то не похожее на число...')
        except TypeError:
            while True:
                try:
                    value = float(input('Попробуй заново ввести число : '))
                except TypeError:
                    print('Что-то ты не то вводишь...')
                    continue
                except ValueError:
                    print('Что-то ты не то вводишь...')
                    continue
                else:
                    break
        finally:
            self.storage[key] = float(value)
            if key == 0 or key == 1:
                self.__init__(self.storage[0], self.storage[1])
            else:
                self.__init__(None, None, self.storage[2], self.storage[3])

    def __str__(self):
        x, y = np.round(self.alg(), 2)
        if y < 0:
            return '{}{}*i'.format(x, y)
        elif y == 0:
            print(x)
        else:
            return '{} + i*{}'.format(x, y)

    def __abs__(self):
        return self.storage[2]



