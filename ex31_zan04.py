# 1. дефиниция на функцията

def show(*, size, ver='1.0'):
     
    print(f'keyword only param size:{size}')
    print(f'keyword-only optional param version:{ver}')

    print()


if __name__ == '__main__':

    # 2. извикване на функцията
    show( size = 10 )
    show( size = 20, ver = '5.0' )
    print('---')