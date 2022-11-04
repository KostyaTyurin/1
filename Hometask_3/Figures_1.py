import math


class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def distance(self, other):
        return ((other.get_y() - self.get_y()) ** 2 + (other.get_x() - self.get_x()) ** 2) ** 0.5

    def __sub__(self, other):
        return Point(self.get_x()-other.get_x(), self.get_y() - other.get_y())

    def __mul__(self, other):
        return self.get_x() * other.get_x() + self.get_y() * other.get_y()

    def __abs__(self):
        return (self.get_x() ** 2 + self.get_y() ** 2) ** 0.5

    def cosinus(self, other):
        return (self * other) / (abs(self) * abs(other))

    def __str__(self):
        return "[" + str(self._x) + ", " + str(self._y) + "]"


class Shape:
    def __init__(self, figure_type="Shape"):
        self._type = figure_type

    def __str__(self):
        return str(self._type)


class Triangle(Shape):
    def __init__(self, p1, p2, p3, figure_type="Triangle"):
        super().__init__(figure_type)
        self._point_1 = p1
        self._point_2 = p2
        self._point_3 = p3
        self._edges = self.edges_len()

    def __str__(self):
        return str(self._type)

    def dots(self):
        return [self._point_1, self._point_2, self._point_3]

    def edges_len(self):
        list_of_edges = []
        list_of_dots = self.dots()
        n = len(list_of_dots)
        for j in range(n-1):
            list_of_edges.append(list_of_dots[j].distance(list_of_dots[j+1]))
        list_of_edges.append(list_of_dots[n-1].distance(list_of_dots[0]))
        return list_of_edges

    def perimetr(self):
        p = 0
        for edge in self._edges:
            p += edge
        return p

    def area_gauss(self):
        n = len(self.dots())
        dots = self.dots()
        res = 0
        for j in range(n-1):
            res += dots[j].get_x()*dots[j+1].get_y() - dots[j+1].get_x()*dots[j].get_y()
        res += dots[n-1].get_x()*dots[0].get_y() - dots[0].get_x()*dots[n-1].get_y()
        return abs(res)/2


class Rectangle(Triangle):
    def __init__(self, p1, p2, p3, p4, figure_type='Rectangle'):
        if (p2-p1).cosinus(p3-p2) == 0 and (p3-p2).cosinus(p4-p3) == 0:
            self._point_4 = p4
            super().__init__(p1, p2, p3, figure_type)
        else:
            print('Фигура не похожа на прямоугольник')

    def dots(self):
        return [self._point_1, self._point_2, self._point_3, self._point_4]


class Square(Rectangle):
    def __init__(self, p1, p2, p3, p4, figure_type='Square'):
        super().__init__(p1, p2, p3, p4, figure_type)
        if abs(p2 - p1) != abs(p3 - p2):
            print('Стороны фигуры не равны между с собой - это не квадрат')


class Rhombus(Triangle):
    def __init__(self, p1, p2, p3, p4, figure_type='Rhombus'):
        if abs(p2 - p1) == abs(p4-p3) and abs(p3 - p2) == abs(p4-p1):
            self._point_4 = p4
            super().__init__(p1, p2, p3, figure_type)
        else:
            print('Это не ромб')

    def dots(self):
        return [self._point_1, self._point_2, self._point_3, self._point_4]


class Circle(Shape):
    def __init__(self, center_point, circle_point, figure_type='Circle'):
        super().__init__(figure_type)
        self._center = center_point
        self._radius = abs(circle_point - center_point)

    def perimetr(self):
        return 2*math.pi * self._radius

    def area(self):
        return math.pi * self._radius**2


a = Triangle(Point(), Point(0, 3), Point(4, 0), 'Triangle')
b = Rectangle(Point(0, 0), Point(0, 2), Point(5, 2), Point(5, 0), 'Rectangle')
c = Square(Point(0, 0), Point(0, 2), Point(2, 2), Point(2, 0), 'Square')
o = Circle(Point(0, 0), Point(1, 0))
r = Rhombus(Point(0, 0), Point(-3, 4), Point(0, 8), Point(3, 4))
print(r.area_gauss())
print(r.perimetr())
