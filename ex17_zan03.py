

if __name__ == '__main__':

    tp = 11, 22, 44, 55, 66

    for item in enumerate(tp, start = 5):
        key, value = item
        print(f'key = {key}, value = {value}')

    print('---')