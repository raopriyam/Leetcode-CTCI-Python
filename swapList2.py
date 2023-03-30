# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 22:15:22 2023

@author: priya
"""

def swapList1(list1):
    n = len(list1)-1
    i = 0
    while i<n:
        temp = list1[i]
        list1[i] = list1[n]
        list1[n] = temp
        i += 1
        n -= 1
    return list1


print(swapList1([1,2,3,4,5,6]))        