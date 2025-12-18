# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 23:39:29 2025

@author: priya
"""

def removeDuplicates(arr):
    set1 = set()
    finalList = []
    for i in arr:
        if i not in set1:
            finalList.append(i)
            set1.add(i)
    return finalList 

print(removeDuplicates([111,2,3,4,2,3,5,4,7,8,6,9,0,2,4,6]))