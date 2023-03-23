# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 23:42:56 2023

@author: priya
"""

def listlen(list1):
    count = 0
    for i in list1:
        count = count+1 
    return count

print(listlen([1,2,4,3,7,6,30,9,8]))
        