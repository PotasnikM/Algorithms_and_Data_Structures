from random import randint
from time import time


# Creating function to sort list A by insertion
def insert_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key


# Creating function to sort list A by merge
def merge_sort(A):
    if len(A) > 1:
        mid = len(A) // 2
        left = A[:mid]
        right = A[mid:]
        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1


if __name__ == '__main__':
    # Creating lists to store the times of each iterations of sorting
    time_insert = []
    time_merge = []
    # Creating for loop to repeat sorting 100-times
    for i in range(100):
        # Creating list of 10^4 random integers from <0,100>
        A_insert = [randint(0, 100) for _ in range(10000)]
        A_merge = A_insert
        # Measuring time of insertion sort
        start_insert = time()
        insert_sort(A_insert)
        end_insert = time()
        # Measuring time of merge sort
        merge_sort(A_merge)
        end_merge = time()
        # Saving the results
        time_insert.append(end_insert - start_insert)
        time_merge.append(end_merge - end_insert)
    # Printing the results
    print('Max time of insert sort is {} and min time is {}'.format(max(time_insert), min(time_insert)))
    print('Average time of insert sort is', sum(time_insert)/len(time_insert))
    print('Time of all iteration of insert sort is', sum(time_insert))
    print('Max time of merge sort is {} and min time is {}'.format(max(time_merge), min(time_merge)))
    print('Average time of merge sort is', sum(time_merge) / len(time_merge))
    print('Time of all iteration of merge sort is', sum(time_merge))
