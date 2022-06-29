# 1. дефиниция на функцията

def sum_numbers(a, b):
    # тяло на функцията
    print(f'{a} + {b} = {a + b}')

if __name__ == '__main__':

    # 2. извикване на функцията
    sum_numbers(5, 6)
    
    x, y = 10, 21
    sum_numbers( x, y)

    print('---')