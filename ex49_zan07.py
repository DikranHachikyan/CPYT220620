
if __name__ == '__main__':
    
    actions = {
        '+': lambda a,b: a + b
    }
    while True:
        try:
            op = input('Action (+, q-quit):')
            if op == 'q':
                # break
                quit()
                
            value1 = float(input('first number:'))
            value2 = float(input('second number:'))
            result = actions[op](value1, value2)
        except ValueError as e:
            print(f'Invalid number: {e}')
        except KeyError as e:
            print(f'Unsupported operation:{e}')
        except Exception as e:
            print(f'Unknown error! ({e})')
        else:
            print(f'{value1} {op} {value2} = {result} ')
            print('--- else ---')
            continue
        finally:
            print('--- finally ---')

    print('---')