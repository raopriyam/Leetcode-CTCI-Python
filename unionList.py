# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 18:34:02 2021

@author: priya
"""

def unionList(arr1,arr2):
    ans = []
    dict1 = {}
    for i in arr1:
        if i not in dict1:
            dict1[i] = 0
            ans.append(i)
    for i in arr2:
        if i not in dict1:
            dict1[i] = 0
            ans.append(i)
    return ans
            
        
        
print(unionList([1,2,3],[3,2,1]))