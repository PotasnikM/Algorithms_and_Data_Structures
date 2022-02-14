import time as t

if __name__ == '__main__':
    L = [1, 2]
    for i in range(100000):                                     # Creating list L
        L.append((L[i] + L[i + 1]) / (L[i + 1] - L[i]))
    sum_of_L_cpp = 0
    s_time_cpp = t.time()
    for i in range(len(L)):                                     # Implementation of for loop like in cpp
        sum_of_L_cpp += L[i]
    time_of_for_cpp = t.time() - s_time_cpp
    sum_of_L_iterable = 0
    s_time_iterable = t.time()
    for elem in L:                                              # Implementation of for loop on iterable object (list L0
        sum_of_L_iterable += elem
    time_of_for_iterable = t.time() - s_time_iterable
    if sum_of_L_iterable == sum_of_L_cpp:
        print('Both implementations give the same result')
    else:
        print('Implementations give different results')
    print('Time of \'for\' loop implemented on the iterated object is ', time_of_for_iterable, 's')
    print('Time of \'for\' loop implemented like in cpp is ', time_of_for_cpp, 's')
