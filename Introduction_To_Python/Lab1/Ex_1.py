from time import *

if __name__ == '__main__':
    s_time = time()
    L = [1, 2]
    for i in range(46):                                                 # Creating list L
        L.append((L[i]+L[i+1])/(L[i+1]-L[i]))
    average_of_L = sum(L) / len(L)                                      # Calculating average value in L
    L.sort()
    median_of_L = (L[23] + L[24]) / 2                                   # Calculating median of values in L
    contains_duplicates = any(L.count(element) > 1 for element in L)    # Checking if L contains duplicates
    print('Average value in L is', average_of_L)
    print('Median in L is', median_of_L)
    print('L contains duplicates:', contains_duplicates)
    print('Time of list method is', time() - s_time)
