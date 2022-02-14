import os
from time import time
import matplotlib.pyplot as plt


def search_naive(pat, matrix):
    n = len(matrix[0])
    m = len(pat[0])
    coordinates = []
    for s in range(n - m):
        for k in range(n - m):
            if pat[0] == matrix[s][k: k + m] and pat[1] == matrix[s + 1][k] and pat[2] == matrix[s + 2][k]:
                coordinates.append((s, k))
    return coordinates


def search_rabin_karp(pat, matrix, d, q):

    n = len(matrix[0])
    m = len(pat[0])
    h = (d ** (m - 1)) % q
    p = []
    t_zero = []
    coordinates = []
    for j in range(m):
        p_ = 0
        t_ = 0
        for i in range(m):
            if j == 0:
                p_ = (d * p_ + int(pat[j][i], 16)) % q
                t_ = (d * t_ + int(matrix[j][i], 16)) % q
            else:
                p_ = (d * p_ + int(pat[j][0], 16)) % q
                t_ = (d * t_ + int(matrix[j][0], 16)) % q
        p.append(p_)
        t_zero.append(t_)
    for s in range(n - m + 1):
        for k in range(n - m + 1):
            if p[0: 2] == t_zero[0: 2]:
                if pat[0] == matrix[s][k:k + m] and pat[1] == matrix[s + 1][k] and pat[2] == matrix[s + 2][k]:
                    coordinates.append((s, k))
            if k < n - m:
                t_zero[0] = (d * (t_zero[0] - int(matrix[s][k], 16) * h) + int(matrix[s][k + m], 16)) % q
                t_zero[1] = int(matrix[s + 1][k + 1], 16) % q
                t_zero[2] = int(matrix[s + 2][k + 1], 16) % q

        t_zero = []
        if s < n - m:
            t_ = 0
            for i in range(m):
                t_ = (d * t_ + int(matrix[s + 1][i], 16)) % q
            t_zero.append(t_)
            t_zero.append(int(matrix[s + 2][0], 16) % q)
            t_zero.append(int(matrix[s + 3][0], 16) % q)
    return coordinates


def make_matrix(path):
    matrix = []
    with open(path, 'r+') as file:
        for line in file:
            matrix.append(line.strip())
    return matrix


if __name__ == '__main__':
    numbers = [1000, 2000, 3000, 4000, 5000, 8000]
    pattern = ['ABC', 'B', 'C']
    time_naive = []
    time_r_k = []
    sum_hits_naive = []
    sum_hits_r_k = []
    for j in numbers:
        path_to_matrix = os.path.abspath('{}_pattern.txt'.format(j))
        matrix_of_data = make_matrix(path_to_matrix)
        s_time_naive = time()
        cords_naive = search_naive(pattern, matrix_of_data)
        time_naive.append(time() - s_time_naive)
        sum_hits_naive.append(len(cords_naive))
        s_time_r_k = time()
        cords_r_k = search_rabin_karp(pattern, matrix_of_data, 16, 2)
        time_r_k.append(time() - s_time_r_k)
        sum_hits_r_k.append(len(cords_r_k))
    for x in range(1):
        print(100 * '#')
        print('Time of naive searching in {}x{} matrix is {} s. Number of spotted patterns {}'
              .format(numbers[x], numbers[x], round(time_naive[x], 6), sum_hits_naive[x]))
        print('Time of Rabin-Karp searching in {}x{} matrix is {} s. Number of spotted patterns {}'
              .format(numbers[x], numbers[x], round(time_r_k[x], 6), sum_hits_r_k[x]))

    x_values = []
    for elem in numbers:
        x_values.append(elem ** 2)

    plt.plot(x_values, time_naive, 'ob', label='Time of naive searching')
    plt.plot(x_values, time_r_k, 'or', label='Time of Rabin-Karp searching')
    plt.ylabel('Time [s]')
    plt.xlabel(' Number of the elements in matrix')
    plt.title('Time dependence on the number of the elements in matrix')
    plt.legend()
    plt.show()
    """pattern = ['ABC', 'B', 'C']
    path_to_matrix = os.path.abspath('1000_pattern.txt')
    matrix_of_data = ['AABC', 'ABCA', 'BCAA', 'CCAA']
    matrix_of_data = make_matrix(path_to_matrix)
    print(search_rabin_karp(pattern, matrix_of_data, 100, 101))"""
