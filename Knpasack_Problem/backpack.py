from time import time
import matplotlib.pyplot as plt


def get_items(path):
    with open(path, 'r') as file:
        next(file)
        next(file)
        items = []
        for line in file:
            items.append(list(map(int, line.strip().split(','))))
        for item in items:
            item.append(item[3] / (item[1] * item[2]))
            item.append(item[1] * item[2])
    return items


def put_in(x, y, matrix_of_backpack, h, w, item):
    value = 0
    area = 0
    for i in range(h):
        for j in range(w):
            if ((h + x) <= len(matrix_of_backpack)) and ((w + y) <= len(matrix_of_backpack)):
                matrix_of_backpack[i + x][j + y] = item[0]
                value = item[3]
                area = item[5]
    return matrix_of_backpack, value, area


def packing(matrix_of_backpack, item):
    temp = False
    value = 0
    area = 0
    for i in range(len(matrix_of_backpack) - item[1] + 1):
        for j in range(len(matrix_of_backpack) - item[2] + 1):
            if sum(matrix_of_backpack[i][j: j + item[2] - 1]) == 0:
                for k in range(item[1]):
                    if matrix_of_backpack[i + k][j] != 0 or matrix_of_backpack[i + k][j + item[2] - 1] != 0:
                        temp = False
                        break
                    else:
                        temp = True
                if temp:
                    matrix_of_backpack, value, area = put_in(i, j, matrix_of_backpack, item[1], item[2], item)
                    break
        if temp:
            break
    if not temp:
        for i in range(len(matrix_of_backpack) - item[2] + 1):
            for j in range(len(matrix_of_backpack) - item[1] + 1):
                if sum(matrix_of_backpack[i][j: j + item[1] - 1]) == 0:
                    for k in range(item[2]):
                        if matrix_of_backpack[i + k][j] != 0 or matrix_of_backpack[i + k][j + item[1] - 1] != 0:
                            temp = False
                            break
                        else:
                            temp = True
                    if temp:
                        matrix_of_backpack, value, area = put_in(i, j, matrix_of_backpack, item[2], item[1], item)
                        break
            if temp:
                break
    return matrix_of_backpack, value, area


if __name__ == '__main__':
    indexes = [20, 100, 500]
    for index in indexes:
        eq = get_items(f'packages{index}.txt')
        backpack = []
        all_val = 0
        all_ar = 0
        start = time()
        for _ in range(index):
            backpack.append([0 for _ in range(index)])
        eq.sort(reverse=True, key=lambda x: x[4])
        for e in eq:
            backpack, val, ar = packing(backpack, e)
            all_val += val
            all_ar += ar
        print(150 * '#')
        print(f'Time to fill {index}x{index} backpack by greedy algorithm is {time() - start} s and value of all items '
              f'in is {all_val}. Backpack is in {(all_ar * 100) / (index * index)}% full.')
        start = time()

        fig, ax = plt.subplots()
        ax.imshow(backpack, cmap=plt.get_cmap('gist_stern'))
        if index == 20:
            for g in range(index):
                for o in range(index):
                    c = backpack[o][g]
                    ax.text(g, o, str(c), va='center', ha='center')
        plt.savefig(f'greedy{index}.png')

        eq.sort(reverse=True, key=lambda x: x[3])
        backpack = []
        for _ in range(index):
            backpack.append([0 for _ in range(index)])
        all_val = 0
        all_ar = 0
        for e in eq:
            backpack, val, ar = packing(backpack, e)
            all_val += val
            all_ar += ar
        print(f'Time to fill {index}x{index} backpack by naive algorithm is {time() - start} s and value of all items '
              f'in is {all_val}. Backpack is in {(all_ar * 100) / (index * index)}% full.')

        fig, ax = plt.subplots()
        ax.imshow(backpack, cmap=plt.get_cmap('gist_stern'))
        if index == 20:
            for g in range(index):
                for o in range(index):
                    c = backpack[o][g]
                    ax.text(g, o, str(c), va='center', ha='center')
        plt.savefig(f'naive{index}.png')
    print(150 * '#')
