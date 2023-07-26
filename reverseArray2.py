# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 19:32:37 2023

@author: priya
"""

def reverseArray(array):
    start = 0
    last = len(array) - 1
    while(last>start):
        temp = array[last]
        array[last] = array[start]
        array[start] = temp
        last -= 1
        start += 1
        
    return array

print(reverseArray([1,2,3,4,5,6,7]))