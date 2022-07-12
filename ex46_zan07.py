
from time import time, sleep
from functools import wraps

def to_uppercase(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.__original = func
        args = [ f'{v}'.upper() for v in args]
        return func(*args, **kwargs)
    return wrapper

if __name__ == '__main__':
    
    print('hello', 'python', 'lorem', 'ipsum')

    print = to_uppercase(print)

    print('hello', 'python', 'lorem', 'ipsum')

    print = print.__original
    
    print('hello', 'python', 'lorem', 'ipsum')


    print('---')