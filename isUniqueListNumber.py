# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 20:38:13 2023

@author: priya
"""

def isUniqueListNumber(list1):
    set1 = set()
    for i in list1:
        if i in set1:
            return False   
        else:
            set1.add(i)
    return True

print(isUniqueListNumber([1,2,3,4,5,6,7,8,9]))