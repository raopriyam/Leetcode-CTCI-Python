# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 22:48:32 2021

@author: priya
"""


def insertion_sort(arr):
    for i in range(1, len(arr)):
        up = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > up:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = up
    return arr


def bucket_sort(numbers):
    arr = []
    slot_num = 10  # 10 means 10 slots, each
    # slot's size is 0.1
    for i in range(slot_num):
        arr.append([])

    # Put array elements in different buckets
    for j in numbers:
        index_b = int(slot_num * j)
        arr[index_b].append(j)

    # Sort individual buckets
    for i in range(slot_num):
        arr[i] = insertion_sort(arr[i])

    # concatenate the result
    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            numbers[k] = arr[i][j]
            k += 1
    return numbers


# Driver Code
if __name__ == '__main__':
    numbers = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    print("Sorted Array is")
    print(bucket_sort(numbers))