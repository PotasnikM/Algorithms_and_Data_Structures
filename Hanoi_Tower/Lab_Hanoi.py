from time import time_ns
import matplotlib.pyplot as plt
# Creating lists to store the moves of both approaches
"""rec_moves = []
it_moves = []"""


# Defining tower of Hanoi recursively
def hanoi_recursive(n, sour, dest, buff):
    if n == 1:
        # rec_moves.append(str(sour) + str(dest))
        return
    hanoi_recursive(n - 1, sour, buff, dest)
    # rec_moves.append(str(sour) + str(dest))
    hanoi_recursive(n - 1, buff, dest, sour)


# Defining tower of Hanoi iteratively
def hanoi_iterative(n):
    if n % 2 == 1:
        for i in range(1, 1 << n):
            if (i & i - 1) % 3 == 0:
                sour = 'S'
            elif (i & i - 1) % 3 == 1:
                sour = 'B'
            else:
                sour = 'D'
            if (i | i - 1) % 3 == 1:
                dest = 'D'
            elif ((i | i - 1) + 1) % 3 == 1:
                dest = 'B'
            else:
                dest = 'S'
            # it_moves.append(str(sour) + str(dest))
    else:
        for i in range(1, 1 << n):
            if (i & i - 1) % 3 == 0:
                sour = 'S'
            elif (i & i - 1) % 3 == 1:
                sour = 'D'
            else:
                sour = 'B'
            if (i | i - 1) % 3 == 1:
                dest = 'B'
            elif ((i | i - 1)+1) % 3 == 1:
                dest = 'D'
            else:
                dest = 'S'
            # it_moves.append(str(sour) + str(dest))


if __name__ == '__main__':
    # Creating lists to store times of each iteration
    times_recursive = []
    times_iterative = []
    sour = 'S'
    buff = 'B'
    dest = 'D'
    # Creating list that store the number of disc in each iteration
    counter = [i for i in range(1, 31)]
    # Loop that compare iterative and recursive approaches
    for n in counter:
        start_recursive = time_ns()
        hanoi_recursive(n, sour, dest, buff)
        start_iterative = time_ns()
        hanoi_iterative(n)
        end_iterative = time_ns()
        times_recursive.append((start_iterative - start_recursive) / 10 ** 9)
        times_iterative.append((end_iterative - start_iterative) / 10 ** 9)
    # Creating plot that shows time dependence on the number of disks in the Hanoi tower
    fig, ax = plt.subplots()
    ax.plot(counter, times_recursive, 'ro', label='Recursive approach')
    ax.plot(counter, times_iterative, 'bo', label='Iterative approach')
    plt.xscale('linear')
    plt.grid(which='both', axis='both')
    plt.ylabel('Time [s]')
    plt.xlabel('Number of discs')
    plt.title('Time dependence on the number of disks in the Hanoi tower')
    plt.legend()
    plt.show()
    # Checking if both approaches makes the same moves
    """if rec_moves == it_moves:
        print('Both approaches gives the same moves')
    else:
        print('Moves are different')"""
    for i in range(9, 30):
        print('Time difference on {} discs is {} s.'.format(i + 1, times_iterative[i] - times_recursive[i]))
