# 1. дефиниция на функцията

# port- глобална променлива
port = 3306

def sum_numbers(a, b, *args):
    # тяло на функцията
    # c - локална променлива
    c = a + b
    print(f'args:{args}')
    for v in args:
        c += v
    return c

if __name__ == '__main__':

    # 2. извикване на функцията
    rs1 = sum_numbers(5, 6)
    
    x, y, z = 10, 21, 4
    rs2 = sum_numbers( x, y, z)

    print(f'rs1 = {rs1} rs2 = {rs2}')
    
    arr = [ 5, 6, 7, 8, 9, 10]

    rs3 = sum_numbers( x, y, *arr)

    print(f'rs3 = {rs3}')
    
    print('---')