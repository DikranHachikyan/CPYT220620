# 1. дефиниция на класа

class Point():
    
    def __init__(self, *, x=0, y=0, **kwargs):
        print('Init Point')
        # данни на обекта
        self.x = x
        self.y = y


    # методи на обекта
    def draw(self):
        print(f'draw point at ({self.x }, {self.y})')
    
    def move_to(self, dx, dy):
        self.x += dx
        self.y += dy

    # методи за достъп до данните
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self,x):
        assert type(x) is int and x >= 0, f'x must be positive int'
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        assert type(y) is int and y >= 0, f'y must be positive int'
        self.__y = y

if __name__ == '__main__':
    # 2. декларация на променлива от типа
    # клас - типът, Point; обект - представител на класа p
    
    p1 = Point( x=10, y=20)

    p1.x = 11
    p1.y = -4

    p1.draw()
    p1.move_to(4,4)
    p1.draw()
    print('---')