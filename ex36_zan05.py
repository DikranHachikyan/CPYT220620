# Глобална променлива


def foo(a=None, b=None):

    if not a: a = []
    if not b: b = {}
    
    print(f'a={a}')
    print(f'b={b}')

    print('-' * 20)
    n = len(a)
    a.append(n)
    b[n] = n

    


if __name__ == '__main__':

    foo()

    foo([3,4,5], {'X': 10})

    foo()

    foo([13,4,15, 3], {'X': 10, 'Y':5})

    foo()
    print('---')