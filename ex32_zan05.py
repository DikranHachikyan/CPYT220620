# Глобална променлива

port = 22

def show():
    global port
    port = 3306
    print(f'port={port}')


if __name__ == '__main__':

    print(f'before:{port}')
    show()
    print(f'alter:{port}')
    print('---')