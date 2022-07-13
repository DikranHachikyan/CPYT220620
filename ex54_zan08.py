# 1. дефиниция на класа

class Point():
    
    def __init__(self):
        print('Init Point')
        # данни на обекта
        self.x = 10
        self.y = 20

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
    

    print(f'Point: ({p.x}, {p.y})')

    p.x = 15
    p.y = 3

    p.draw()
    p.move_to(-10, 20)
    p.draw()
    
    print('---')