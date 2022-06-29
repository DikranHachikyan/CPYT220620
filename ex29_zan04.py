# 1. дефиниция на функцията

def show(title, ver='1.0', *args, **kwargs):
    
    print(f'positional:{title}')

    print(f'optional version:{ver}')

    print(f'args:{args}')
    for v in args:
        print(v, end=' ')
    print()
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
    show('Text Editor', *margins)

    show('Text Editor')
    
    print('---')