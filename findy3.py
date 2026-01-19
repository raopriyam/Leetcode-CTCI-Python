# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 11:23:31 2026

@author: priya
"""

def findY3(grid, yval, nonyval):
    n = len(grid)
    mid = n // 2
    operations = 0
    
    for row in range(n):
        for col in range(n):
            
            is_y = (
                (row <= mid and col == row) or
                (row <= mid and col == n - (row+1)) or
                (row >= mid and col == mid)
                )
            
            target = yval if is_y else nonyval
            
            if grid[row][col] != target:
                operations += 1
                
    return operations