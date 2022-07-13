# 1. дефиниция на класа

class Point():
    
    def __init__(self, *, x=0, y=0, **kwargs):
        print('Init Point')
        # данни на обекта
        self.x = x
        self.y = y

    # методи на обекта
    def draw(self):
        print(f'draw point at ({self.x}, {self.y})')
    
    def move_to(self, dx, dy):
        self.x += dx
        self.y += dy

if __name__ == '__main__':
    # 2. декларация на променлива от типа
    # клас - типът, Point; обект - представител на класа p
    p = Point()
    p2 = Point( x=10, y=20)


    p.draw()
    p.move_to(-5, 2)
    p.draw()

    p2.draw()
    
    print('---')