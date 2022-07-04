# Глобална променлива

# 1 + 2 + 3 + ... + n

def sum_n(n):
    print(f'n={n}')
    if n > 0:
        return n + sum_n( n - 1)
    return 0

if __name__ == '__main__':

    res = sum_n(3)
    print(f'result = {res}')
    print('---')