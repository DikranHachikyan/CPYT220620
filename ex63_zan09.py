# 1. дефиниция на класа

import draw.point as dp



if __name__ == '__main__':
    # 2. декларация на променлива от типа
    p1 = dp.Point(x=10, y=20)

    p1.draw()
    p2 = dp.Point(x=1, y=2)
    p1.draw()

    print('---')