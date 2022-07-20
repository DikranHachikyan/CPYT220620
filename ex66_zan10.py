# 1.
# import draw.point as dp

# 2.

from draw import Rectangle, ShapeMixin


class CRectangle(Rectangle,ShapeMixin):
    pass

if __name__ == '__main__':
    
    crc = CRectangle(x=10, y=20, width=100, height=20)

    crc.draw()

    s = crc.get_area()

    print(f's={s}')

    print('---')