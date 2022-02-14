import array as arr
import numpy as np
from time import *

if __name__ == '__main__':
    s_time = time()
    L = arr.array('d', [1.0, 2.0])
    for i in range(46):                                                             # Creating list L
        L.append((L[i]+L[i+1])/(L[i+1]-L[i]))
    average_of_L = sum(L) / len(L)                                                  # Calculating average value in L
    sorted_L = np.sort(L)
    median_of_L = (sorted_L[23] + sorted_L[24]) / 2                                 # Calculating median of values in L
    contains_duplicates = any(L.count(element) > 1 for element in L)                # Checking if L contains duplicates
    print('Average value in L is', average_of_L)
    print('Median in L is', median_of_L)
    print('L contains duplicates: ', contains_duplicates)
    print('Time of array method is', time() - s_time)
