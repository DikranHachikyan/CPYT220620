# Глобална променлива


def sort_priority(values, grp):
    found = False
    
    def sort_helper(el):
        nonlocal found
        if el in grp:
            found = True
            return (0, el)
        return (1, el)


    values.sort(key = sort_helper )

    return found


if __name__ == '__main__':

    numbers = [ 5, 4, 6, 3, 7, 9, 8]
    grp = {8,4,9}

    is_found = sort_priority(numbers, grp)

    print(f'numbers={numbers} is_found:{is_found}')
    print('---')