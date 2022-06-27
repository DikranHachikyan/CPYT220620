

if __name__ == '__main__':
    #  1 + 2 + 3 + 4 + ... + 99 + 100 = 5050

    i = 0
    sum_n = 0

    is_interrupted = True

    while i <= 100:
        i += 1

        if i == 20:
            break

        sum_n += i
    else:
        is_interrupted = False

    print(f'1 + 2 + 3 + ... + 99 + 100 = {sum_n} status:{is_interrupted}')
    print('---')