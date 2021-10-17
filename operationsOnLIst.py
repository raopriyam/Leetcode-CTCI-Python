# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 16:20:34 2021

@author: priya
"""

arr = [5,3,2,1,3]
operations = [[0,1],[1,3]]


for i in operations:
    left = i[0]
    right = i[-1]
    #print(left)
    #print(right)
    while left<right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1 
    print(arr)