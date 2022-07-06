
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
from functools import wraps

def measure(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        t = time()
        func(*args, **kwargs)
        print(f'{func.__name__} time:{time() - t:.3f}')
    
    return wrapper

@measure
def foo(sleep_time=0.5):
    '''Function foo sleeps sleep_time seconds'''
    sleep(sleep_time)



if __name__ == '__main__':

    foo()
    foo(0.3)
    print(f'name:{foo.__name__} doc:{foo.__doc__}')
 
    print('---')