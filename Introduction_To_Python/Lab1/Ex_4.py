if __name__ == '__main__':
    list_ = [1, 2, 3]
    try:
        print(list_[3])
    except IndexError:
        print('Out of index')
    try:
        x = 1/0
    except ZeroDivisionError:
        print('Division by 0')
    try:
        array.list_
    except NameError:
        print('Function not found')
