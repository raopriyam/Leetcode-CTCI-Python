# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 18:43:57 2021

@author: priya
"""

def check(x,op):
    #x = [5,3,2,1,3]
    #y = [[0,1],[1,3]]
    
    
    for y in op:
        left = y[0]
        right = y[-1]
        while(left<right):
            temp = x[left]
            x[left] = x[right]
            x[right] = temp
            left += 1
            right -= 1 
    
    print( x)

check([5,3,2,1,3],[[0,2],[1,3]])


    
    