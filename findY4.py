# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 13:22:56 2026

@author: priya
"""

def findY(grid):
    n = len(grid)
    mid = n // 2
    y_count = [0,0,0]
    non_y_count = [0,0,0]
    
    for row in range(n):
        for col in range(n):
            
            is_y = (
                (row <= mid and col == row) or
                (row <= mid and col == n - 1 - row) or
                (row >= mid and col == mid)
                
                )
            
            v = grid[row][col]
            
            if is_y:
                y_count[v] += 1
            else:
                non_y_count[v] += 1
                
            
    y_total = sum(y_count)
    non_y_total = sum(non_y_count)
    
    ans = float('inf')
    
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            
            ops = (y_total -y_count[i]) + (non_y_total -non_y_count[j])
            ans = min(ans,ops)
            
    return ans
            
