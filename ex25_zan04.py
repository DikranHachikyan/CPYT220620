# 1. дефиниция на функцията

# port- глобална променлива
port = 3306

def sum_numbers(a, b, d = 0):
    # тяло на функцията
    # c - локална променлива
    c = a + b + d
    return c

if __name__ == '__main__':

    # 2. извикване на функцията
    rs1 = sum_numbers(5, 6)
    
    x, y, z = 10, 21, 4
    rs2 = sum_numbers( x, y, z)

    print(f'rs1 = {rs1} rs2 = {rs2}')
    
    print('---')