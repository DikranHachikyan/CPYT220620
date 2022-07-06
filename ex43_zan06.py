
from time import time, sleep
from functools import wraps

def to_string(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args = [ f'{v}' for v in args]
        return func(*args, **kwargs)
    return wrapper

def add_brackets(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args = [ f'[{v}]' for v in args]
        return func(*args, **kwargs)
    return wrapper

@add_brackets
@to_string
def concat(*args, **kwargs):
    '''Concatenate list of elements with separator sep'''
    sep = kwargs.get('sep',';')
    return sep.join(args)

if __name__ == '__main__':
    users = ['anna', 'maria', 'markus','jorg']

    print(concat(*users))
    print(concat(*users, sep=','))

    values = [1, 12, 45, 67, 89]
    print(concat(*values, sep='|'))

    print('---')