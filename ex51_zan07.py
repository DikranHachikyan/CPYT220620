def print_key(key, **kwargs):
    try:
        print(f'{key} => {kwargs[key]}')
    except KeyError as e:
        # 3. добро решение
        raise
        # 2. не е добра идея
        # pass
        
        # 1. не е добра идея
        # print(f'invalid key:{e}')

if __name__ == '__main__':
    conn = {
        'host':'localhost',
        'port':1521,
        'service':'oracle'
    }
    try:
        print_key('host', **conn)
        print_key('ip', **conn)
    except KeyError as e:
        print(f'invalid key:{e}')
    print('---')