
# 1.
# import time
# print(f'now:{time.time()}')

# 1.1
# import time as tm
# print(f'now:{tm.time()}')

# 2.
# from time import time, sleep
# print(f'now:{time()}')

# 2.1
# from time import time as now, sleep
# print(f'now:{now()}')

from time import time, sleep


def foo():
    sleep(0.5)

def bar():
    sleep(0.3)

if __name__ == '__main__':

    t = time()
    foo()
    print(f'time:{time() - t:.3f}')
    
    t = time()
    bar()
    print(f'time:{time() - t:.3f}')

    print('---')