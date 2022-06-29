# 1. дефиниция на функцията

def show(title, *args, size, ver='1.0', **kwargs):
    
    print(f'positional:{title}')


    print(f'args:{args}')
    for v in args:
        print(v, end=' ')
    print()
    
    print(f'keyword only param size:{size}')
    print(f'keyword-only optional param version:{ver}')

    props = {
        'c': kwargs.get('color', 'black'),
        'f': kwargs.get('font', 'sans-serif')
    }
    print(f"color is {props['c']} and font is {props['f']}")
    print()


if __name__ == '__main__':

    # 2. извикване на функцията

    margins = [5, 10, 5, 10]
    # на параметъра ver не му работи подр. стойност 
    show('Text Editor', *margins, size = 10, ver = '2.0')

    show('Text Editor', size = 20)

    show('Text Editor', size = 30, ver = '3.0')
    
    print('---')