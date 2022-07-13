# 1. дефиниция на класа

class Point():
    
    def __init__(self, *, x=0, y=0, visible=True, **kwargs):
        print('Init Point')
        # данни на обекта
        self.set_x(x)
        self.set_y(y)
        self.set_visible(visible)

    # методи на обекта
    def draw(self):
        print(f'draw point at ({self.get_x()}, {self.get_x()})')
    
    def move_to(self, dx, dy):
        self.set_x( self.get_x() + dx)
        self.set_y( self.get_y() + dy)

    # методи за достъп до данните

    def set_x(self, x):
        assert x >= 0, f'x must be positive number: ({x})' 
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def set_visible(self, visible):
        self.__visible = visible

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y    

    def is_visible(self):
        return self.__visible

if __name__ == '__main__':
    # 2. декларация на променлива от типа
    # клас - типът, Point; обект - представител на класа p
    
    p1 = Point( x=10, y=20)

    if p1.is_visible():
        p1.draw()

    p1.set_x(12)

    p1.draw()
    
    p1.set_x(-1)
    
    print('---')