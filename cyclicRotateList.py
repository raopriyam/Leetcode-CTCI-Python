# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 18:37:42 2021

@author: priya
"""

def cyclicClockRotateList(arr,n):
    for i in range(n):
        arr.insert(0,arr[-1])
        arr.pop(-1)
    return arr

def cyclicAntiClockRotateList(arr,n):
    ln = len(arr)
    for i in range(n):
        arr.insert(ln,arr[0])
        arr.pop(0)
        print()
        print(arr)
    return arr

print(cyclicClockRotateList([9, 8, 7, 6, 4, 2, 1, 3],3))

print(cyclicAntiClockRotateList([9, 8, 7, 6, 4, 2, 1, 3],3))