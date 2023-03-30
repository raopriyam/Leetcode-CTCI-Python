# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 22:12:40 2023

@author: priya
"""

def swapList(list1):
    n = len(list1)
    temp = list1[0]
    list1[0] = list1[n-1]
    list1[n-1] = temp
    return list1

print(swapList([1,2,3,4,5,6,7]))
    