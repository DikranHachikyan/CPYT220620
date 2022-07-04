# Глобална променлива

# 1 + 2 + 3 + ... + n



if __name__ == '__main__':

    pow_xy = lambda x,y : x ** y

    z = pow_xy( 2, 4 )
    print(f'z = {z}')

    numbers = [ 3, 4, 5, 6, 7]

    for n in map( lambda el: el ** 2 , numbers):
        print(f'n={n}')

    print('---')