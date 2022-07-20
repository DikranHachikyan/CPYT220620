# 1.
# import draw.point as dp

# 2.

from draw import Point



if __name__ == '__main__':

    p = Point(x = 10, y = 20)

    p2 = Point.from_point(p)

    p2.draw()     

    print('---')