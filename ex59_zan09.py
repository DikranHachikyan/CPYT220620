# 1. дефиниция на класа

class Point():
    
    def __init__(self, *, x=0, y=0, **kwargs):
        print('Init Point')
        # данни на обекта
        self.__x = x
        self.__y = y

    # методи на обекта
    def draw(self):
        print(f'draw point at ({self.__x}, {self.__y})')
    
    def move_to(self, dx, dy):
        self.__x += dx
        self.__y += dy

if __name__ == '__main__':
    # 2. декларация на променлива от типа
    # клас - типът, Point; обект - представител на класа p
    
    p1 = Point( x=10, y=20)

    p2 = Point( x=1, y=3)

    # динамично добавя x
    p1.x = 12

    # 1. Ok!
    print(f'point:({p1.x})')
    # print(f'point:({p2.x})')
    
    # 2. Ok!
    # print(f'point:({p1._x})')
    
    # 3. AttributeError
    # print(f'point:({p1.__x})')

    p1.draw()

    
    
    print('---')