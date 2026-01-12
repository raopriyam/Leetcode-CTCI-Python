# -*- coding: utf-8 -*-
"""
Created on Sun Jan 11 22:10:13 2026

@author: priya
"""

def sumDifference():
    array1 = [1,2,-3,4,5,6,-7,8,9]
    oddsum = 0
    evensum = 0
    
    for i in range(len(array1)):
        if i%2 == 0:
            if array1[i] < 0:
                pass
            else:
                evensum = evensum + array1[i]
        else:
            if array1[i] < 0:
                pass
            else:
                oddsum = oddsum + array1[i]
            
    return evensum - oddsum
            

print(sumDifference())