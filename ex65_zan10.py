# 1.
# import draw.point as dp

# 2.
from draw import Point
from draw import Rectangle



if __name__ == '__main__':
    shapes = [
        Rectangle(x=10, y=20, width=300, height=400),
        Point(x=2, y=5),
        Rectangle(x=20, y=10, width=230, height=100),
        Point(x=12, y=51)
    ]
    
    for sh in shapes:
        sh.move_to(100,200)
        sh.draw()
    

    print('---')