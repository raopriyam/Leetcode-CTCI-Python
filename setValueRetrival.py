# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 22:35:36 2023

@author: priya
"""

def setValueRetrival(set1,n):
    if n in set1:
        check = True
    else:
        check = False
        
    if check == True:
        return n
    
    return "Doesn't belong in set"

print(setValueRetrival({1,2,3,4,5,6,7,8,9,10}, 66))
        
    