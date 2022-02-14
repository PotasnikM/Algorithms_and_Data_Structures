import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
from time import time
from ACO import ACO, Graph


def make_city_matrix():
    matrix_of_cities = []
    with open('TSP.txt', 'r') as file:
        for line in file:
            matrix_of_cities.append(line.split())
    return matrix_of_cities


def make_distance_dict():
    matrix_of_cities = make_city_matrix()
    matrix_of_costs = []
    for j in range(len(matrix_of_cities)):
        matrix_of_costs.append([j + 1000])
        for i in range(len(matrix_of_cities)):
            dist = abs((float(matrix_of_cities[j][1]) - float(matrix_of_cities[i][1])) ** 2 +
                       ((float(matrix_of_cities[j][2]) - float(matrix_of_cities[i][2])) ** 2)) ** 0.5
            if dist != 0:
                dist = round(dist, 3)
            else:
                dist = 10001
            matrix_of_costs[j].append(dist)
    return matrix_of_costs


def length_of_path(vector, matrix_of_costs):
    length = 0
    for i in range(len(vector) - 1):
        length += matrix_of_costs[vector[i] - 1][vector[i + 1]]
    return round(length, 3)


def path_(city, matrix_of_costs):
    path_to_cities = [city]
    while len(path_to_cities) != 100:
        index = matrix_of_costs[path_to_cities[-1] - 1].index(min(matrix_of_costs[path_to_cities[-1] - 1]))
        if index in path_to_cities:
            matrix_of_costs[path_to_cities[-1] - 1][index] = 10000
        else:
            path_to_cities.append(index)
    path_to_cities.append(city)
    return path_to_cities


if __name__ == '__main__':
    cost_aco = []
    cost_greedy = []
    time_aco = []
    time_greedy = []
    # print(make_city_matrix())
    for x in range(10):
        start_aco = time()
        costs = make_distance_dict()
        """cords = []
        codes = []
        cities = make_city_matrix()"""

        costs_aoc = costs.copy()
        for row in costs_aoc:
            del row[0]

        aco = ACO(10, 100, 1.0, 10.0, 0.5, 10, 2)
        graph = Graph(costs_aoc, 100)
        path, cost = aco.solve(graph)
        path.append(path[0])
        time_aco.append(time() - start_aco)
        cost_aco.append(cost)
        # Code to print path of aco algorithm
        """for elem in path:
            cords.append((float(cities[elem][1]), float(cities[elem][2])))
        codes.append(Path.MOVETO)
        for _ in range(len(path) - 2):
            codes.append(Path.LINETO)
        codes.append(Path.CLOSEPOLY)
        path_n = Path(cords, codes)
        fig, ax = plt.subplots()
        patch = patches.PathPatch(path_n, facecolor='none', lw=1)
        ax.add_patch(patch)
        for k in range(len(cords)):
            plt.plot(cords[k][0], cords[k][1], 'o')
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        plt.grid(True)
        plt.savefig('aco.png')"""

        cords = []
        codes = []
        start_greedy = time()
        cities = make_city_matrix()
        costs = make_distance_dict()
        p = path_(1, costs)
        time_greedy.append(time() - start_greedy)
        cost_greedy.append(length_of_path(p, costs))
        # Code to print path of greedy algorithm
        for elem in p:
            cords.append((float(cities[elem - 1][1]), float(cities[elem - 1][2])))
        codes.append(Path.MOVETO)
        for _ in range(len(cords) - 2):
            codes.append(Path.LINETO)
        codes.append(Path.CLOSEPOLY)
        path_g = Path(cords, codes)
        fig, ax = plt.subplots()
        patch = patches.PathPatch(path_g, facecolor='none', lw=1)
        ax.add_patch(patch)
        for k in range(len(cords)):
            plt.plot(cords[k][0], cords[k][1], 'o')
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        plt.grid(True)
        plt.savefig('greedy.png')
    print('Average length of path from greedy algorithm is {} and average time needed to calculate this is {} s.'
          .format(round(sum(cost_greedy)/len(cost_greedy), 3), round(sum(time_greedy)/len(time_greedy), 3)))
    print('Average length of path from ant colony optimization algorithm is {} and average time needed to '
          'calculate this is {} s.'
          .format(round(sum(cost_aco)/len(cost_aco), 3), round(sum(time_aco)/len(time_aco), 3)))
    # print(path_(1, make_distance_dict()))
