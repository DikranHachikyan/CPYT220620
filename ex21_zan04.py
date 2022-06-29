

if __name__ == '__main__':

    sq = [ x ** 2 for x in range( 1, 11 )]

    print(f'values={sq}')

    txt = 'Lorem ipsum dolor sit amet'

    symbols = [ f'-{s}-' for s in txt]
    print(f'sym:{symbols}')

    # for i in range(3):
    #     for j in range(4):
    #         print(f'i={i} j={j}')

    values = [ f'i={i} j={j}' for i in range(3) for j in range(4)]

    print(f'values={values}')

    print('---')