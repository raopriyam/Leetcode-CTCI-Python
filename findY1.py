# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 08:30:33 2026

@author: priya
"""

def findY(n):
    left = [0,0]
    right = [0,n-1]
    mid = n//2
    count = 0
    for i in range(mid):
        left[0] += 1
        left[1] += 1
        right[0] += 1
        right[1] -= 1
        count += 2
    count += 1
    
    count += (n-mid-1)
    
    return count

print(findY(3))


