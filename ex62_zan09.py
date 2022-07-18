# 1. дефиниция на класа
from math import sqrt

class Point():
    # данни на класа (статични данни)
    count = 0

    def __init__(self, *, x=0, y=0, **kwargs):
        print('Init Point')
        # данни на обекта
        self.x = x
        self.y = y
        Point.count += 1


    # методи на обекта
    def draw(self):
        print(f'draw point at ({self.x }, {self.y}) count:{Point.count}')
    
    def move_to(self, dx, dy):
        self.x += dx
        self.y += dy

    # методи за достъп до данните
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self,x):
        assert isinstance(x, (int,float) ) and x >= 0, f'x must be positive int'
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        assert isinstance(y, (int,float) ) and y >= 0, f'y must be positive int'
        self.__y = y

    # Специални методи
    #
    # предефиниране на метод (function overriding) 
    def __str__(self):
        return f'({self.x},{self.y})'

    def __eq__(self, other):
        # self.x -> p1
        # other.x -> p2
        if not isinstance(other, Point):
            raise NotImplementedError('Not yet implemented')
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        if not isinstance(other, Point):
            raise NotImplementedError('Not yet implemented')
        dx1 = self.x ** 2
        dy1 = self.y ** 2

        dx2 = other.x ** 2
        dy2 = other.y ** 2

        dist1 = sqrt(dx1 + dy1)
        dist2 = sqrt(dx2 + dy2)
        return dist1 > dist2

    def __add__(self, other):
        if isinstance(other, Point):
            new_x = self.x + other.x
            new_y = self.y + other.y
            # self.x += other.x
        elif isinstance(other, (float, int)):
            new_x = self.x + other
            new_y = self.y + other
        else:
            raise NotImplementedError('Not yet implemented')

        return Point(x=new_x, y=new_y) 

    def __del__(self):
        Point.count -= 1
        print(f'object {self} destroyed {Point.count}')


def show():
    p = Point()
    p.draw()
    print(f'show:{p}')

if __name__ == '__main__':
    # 2. декларация на променлива от типа
    p1 = Point(x=10, y=20)

    p1.draw()
    show()
    p2 = Point(x=1, y=2)
    p1.draw()

    print('---')