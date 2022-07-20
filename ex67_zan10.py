# 1.
# import draw.point as dp

# 2.

from math import sqrt
from draw import Point, Rectangle

class ShapeUtils():
    p0 = Point()

    @staticmethod
    def distance(p1, p2):
        if not isinstance(p1, Point) or not isinstance(p2, Point):
            raise TypeError(f'p1 or p2 is not instance of Point')
        dx = (p1.x - p2.x) ** 2 
        dy = (p1.y - p2.y) ** 2

        return  sqrt(dx + dy)

    @staticmethod
    def compare(p1,p2):
        '''
            Return:
            neg. value if p1 < p2
            zero       if p1 = p2
            pos. value if p1 > p2
        '''
        dist1 = ShapeUtils.distance(p1, ShapeUtils.p0)
        dist2 = ShapeUtils.distance(p2, ShapeUtils.p0)

        return dist1 - dist2

if __name__ == '__main__':
    p1 = Point(x = 9, y = 8)
    p2 = Point(x = 6, y = 4)

    print(f'dist btw {p1} and {p2} is {ShapeUtils.distance(p1,p2)}')
   
    if ShapeUtils.compare(p1,p2) > 0:
        print(f'{p1} > {p2}')

    rc1 = Rectangle()
    rc2 = Rectangle(x=10, y=20, width=100, height=20)

    print(f'dist btw {rc1} and {rc2} is {ShapeUtils.distance(rc1,rc2)}') 

    print('---')