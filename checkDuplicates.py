# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 16:12:35 2021

@author: priya
"""

def checkDuplicates(arr1,arr2,arr3):
    dict1= {}
    ans = []
    ans2 = []
    for i in arr1:
        if i not in dict1:
            dict1[i] = 0
    
    for i in arr2:
        if i not in dict1:
            pass
        else:
            ans.append(i)
    for i in arr3:
        if i in dict1:
            pass
        else:
            ans.append(i)
    for i in ans:
        if i in dict1:
            ans2.append(i)
        
    return ans2
            
print(checkDuplicates([1, 5, 10, 20, 40, 80],[6, 7, 20, 80, 100],
                      [3, 4, 15, 20, 30, 70, 80, 120]))