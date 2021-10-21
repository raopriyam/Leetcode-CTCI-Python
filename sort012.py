# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 03:01:31 2021

@author: priya
"""

def sort012(arr):
    point0 = arr.count(0)
    point1 = arr.count(1)
    point2 = arr.count(2)
    ans = []
    ans.extend([0]*point0)    
    ans.extend([1]*point1)  
    ans.extend([2]*point2)  
    return ans
            

print(sort012([0,3,1,2,1,0,2,1,0,0,0,1,2]))
print(sort012([0 ,2 ,1 ,2 ,0]))

