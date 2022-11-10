import pickle
import numbers


class Pair:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def __add__(self, other):
        if isinstance(other, numbers.Number):
            return Pair(self._x + other, self._y + other)
        if isinstance(other, Pair):
            return Pair(self._x + other.get_x(),
                        self._y + other.get_y())
        return False

    def __str__(self):
        return str(self._x) + " " + str(self._y)


p = Pair(2, 3)
d = {1: [3], "acc": (3, 7)}
with open("pickle_data.bin", mode="wb") as f:
    pickle.dump(p, f)

with open("pickle_data.bin", mode="rb") as f:
    a = pickle.load(f)
print(type(a), a)
