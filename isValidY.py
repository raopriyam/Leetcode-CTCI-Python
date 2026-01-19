# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 11:00:13 2026

@author: priya
"""

def isvalidY(grid):
    n = len(grid)
    mid = n // 2
    yVal = set()
    nyVal = set()
    for row in range(n):
        for col in range(n):
            is_y = (
                ( row <= mid and col == row) or
                (row <= mid and col == n-(row+1)) or
                (row > mid and col == mid)
                )
            
            if is_y:
                yVal.add(grid[row][col])
            else:
                nyVal.add(grid[row][col])
                
        return len(yVal) == 1 and len(nyVal) == 1 and yVal != nyVal
                
            
            
grid1 = [
    [1, 2, 2],
    [2, 1, 2],
    [2, 1, 2]
]

print(isvalidY(grid1))
            