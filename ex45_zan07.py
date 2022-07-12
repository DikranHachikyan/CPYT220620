
from time import time, sleep
from functools import wraps

def to_uppercase(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.__original = func
        args = [ f'{v}'.upper() for v in args]
        return func(*args, **kwargs)
    return wrapper

@to_uppercase
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

    print(concat.__original(*users))

    concat = concat.__original
    print(concat(*users, sep=','))

    # values = [1, 12, 45, 67, 89]
    # print(concat(*values, sep='|'))


    print('---')