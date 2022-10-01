class Complex():

    def __init__(self, x, y, r=None, fi=None):
        self.set(x,y,r , fi)


    def set(self, x, y, r, fi):
        self._x = x
        self._y = y
        self._r = r
        self._fi = fi


    def get_alg(self):
        return self._x, self._y

    def get_exp(self):
        return self._r, self._fi


    def exp(self):
        r = math.sqrt((self._x**2) + (self._y)**2)
        cos_fi = self._x/r
        sin_fi = self._y/r
        fi = math.acos(cos_fi)
        return r, fi


    def alg(self):
        r, fi = self.get_exp()
        a = r*math.cos(fi)
        b = r*math.sin(fi)
        return a, b


    def __add__(self, other):
        if (self._x and self._y) and (other._x and other._y) != None:
            self._x += other._x
            self._y += other._y
            return Complex(self._x, self._y)
        elif (self._r and self._fi) and (other._r and other._fi) != None:
            self._x, self._y = self.alg()
            other._x, other._y = other.alg()
            self._x += other._x
            self._y += other._y
            return Complex(self._x, self._y)
        else:
            raise ValueError('Only one form')

    def __sub__(self, other):
        if (self._x and self._y) and (other._x and other._y) != None:
            self._x -= other._x
            self._y -= other._y
            return Complex(self._x, self._y)
        elif (self._r and self._fi) and (other._r and other._fi) != None:
            self._x, self._y = self.alg()
            other._x, other._y = other.alg()
            self._x -= other._x
            self._y -= other._y
            return Complex(self._x, self._y)
        else:
            raise ValueError('Only one form')

    def __mul__(self, other):
        if self._x != None and self._y != None and other._x != None and other._y != None:
            self._r, self._fi = self.exp()
            other._r, other._fi = other.exp()
            self._r *= other._r
            self._fi += other._fi
            return Complex(self._r, self._fi)
        elif self._r != None and self._fi != None and other._r != None and other._fi != None:
            self._r *= other._r
            self._fi += other._fi
            return Complex(None, None, self._r, self._fi)
        else:
            raise ValueError('Only one form')

    def __truediv__(self, other):
        if self._x != None and self._y != None and other._x != None and other._y != None:
            self._r, self._fi = self.exp()
            other._r, other._fi = other.exp()
            self._r /= other._r
            self._fi -= other._fi
            return Complex(None, None, self._r, self._fi)
        elif self._r != None and self._fi != None and other._r != None and other._fi != None:
            self._r /= other._r
            self._fi -= other._fi
            return Complex(None, None, self._r, self._fi)
        else:
            raise ValueError('Only one form')




import math

a = Complex(None,None, 3, 1)
b = Complex(None, None, 3,5)
c = Complex(1,2)
d = Complex(3,4)
print((c*d).get_alg())
print((a/b).get_exp())
