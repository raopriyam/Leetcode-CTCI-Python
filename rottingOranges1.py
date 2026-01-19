# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 14:36:41 2026

@author: priya
"""

def rottingOranges1(grid):
    n = len(grid)
    m = len(grid[0])
    count= 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                count += 1
    return count