# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 22:18:09 2023

@author: priya
"""

def swapList3(list1):
    i = 0
    n = len(list1)-1 
    while i<n:
        list1[i],list1[n] = list1[n],list1[i]
        i += 1
        n -= 1
    return list1

print(swapList3([1,2,3,4,5]))