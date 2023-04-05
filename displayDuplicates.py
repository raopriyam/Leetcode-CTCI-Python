# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 21:42:02 2023

@author: priya
"""

def findDuplicates(list1):
    dict1 = {}
    for i in list1:
        if i not in dict1:
            dict1[i] = 1 
        else:
            dict1[i] += 1
    return dict1

def removeNonDuplicates(list1):
    dict1 = findDuplicates(list1)
    for i in list1:
        if dict1[i]==1:
            del dict1[i]
            
    return dict1


        
    
    
print(removeNonDuplicates([1,2,3,2,4,5,3,6,7,8,7,9,10]))