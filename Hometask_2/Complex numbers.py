class Complex():

    def __init__(self, x, y, r=None, fi=None):
        self.set(x, y, r, fi)
        if self.storage[0] is not None and self.storage[1] is not None:
            r, fi = self.exp()
        elif self.storage[2] is not None and self.storage[3] is not None:
            x, y = self.alg()
        self.storage = {0: x, 1: y, 2: r, 3: fi}

    def set(self, x, y, r, fi):
        self.storage = {0: x, 1: y, 2: r, 3: fi}

    def get_alg(self):
        return self.storage[0], self.storage[1]

    def get_exp(self):
        return self.storage[2], self.storage[3]

    def exp(self):
        x, y = self.get_alg()
        r = math.sqrt((x**2) + (y)**2)
        cos_fi = x/r
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
            return Complex(x1 + other, y1)

    def __radd__(self, other):
        x1, y1 = self.get_alg()
        return Complex(other + x1, y1)

    def __sub__(self, other):
        x1, y1 = self.get_alg()
        x2, y2 = other.get_alg()
        return Complex(x1 - x2, y1 - y2)

    def __mul__(self, other):
        r1, fi1 = self.get_exp()
        r2, fi2 = other.get_exp()
        return Complex(None, None, r1 * r2, fi1 + fi2)

    def __truediv__(self, other):
        r1, fi1 = self.get_exp()
        r2, fi2 = other.get_exp()
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
        self.storage[key] = value
        if key == 0 or key == 1:
            self.__init__(self.storage[0], self.storage[1])
        else:
            self.__init__(None, None, self.storage[2], self.storage[3])
        # self.__init__()

    def __str__(self):
        x, y = np.round(self.alg(), 2)
        if y < 0:
            # return f'${0}{1}\cdot i$'.format(x,y)
            return ('{}{}*i'.format(x, y))
        elif y == 0:
            print(x)
        else:
            # return r'${0}+{1}\cdot i$'.format(x, y)
            return('{} + i*{}'.format(x, y))

    def __abs__(self):
        return self.storage[2]


import math
import numpy as np

a = Complex(None, None, 3, 1)
b = Complex(None, None, 10, 5)
c = Complex(3,1)

print((5+c))
