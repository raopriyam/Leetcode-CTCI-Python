# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 22:04:33 2026

@author: priya
"""

def findY(n):
    mid = n // 2
    cells = set()
    
    for i in range(mid+1):
        cells.add((i,i))
        cells.add((i,n-(i+1)))
        
    for i in range(mid,n):
        cells.add((i,mid))
        
    return len(cells)

print(findY(5))
        