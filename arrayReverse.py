# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 23:42:42 2021

@author: priya
"""

def arrayReverse(arr):
    left = 0
    right = len(arr)-1
    while left<right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1
    return arr

print(arrayReverse([1,2,3,4,5,0,7,4,9,1,23]))