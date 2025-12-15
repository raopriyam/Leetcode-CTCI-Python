# -*- coding: utf-8 -*-
"""
Created on Sun Dec 14 23:44:55 2025

@author: priya
"""

def MininList(list1):
    minVal = float('inf')
    
    for i in list1:
        if i < minVal:
            minVal = i
            
    return minVal 


print(MininList([4,5,6,1,3,2,8,9,100]))