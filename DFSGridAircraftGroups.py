# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 23:02:22 2023

@author: priya
"""

# Given an aircraft battle group layout, where 1 represents the aircraft and 0 represents the sky, count the number of aircraft battle groups.
# Description: Each aircraft battle group consists of adjacent aircraft in either a horizontal or vertical direction

# input：grid = 
# [
#   [1, 1, 0, 0, 0],
#   [1, 1, 0, 0, 0],
#   [0, 0, 1, 0, 0],
#   [0, 0, 0, 1, 1]
# ]
# output：3

grid =  [
   [1, 1, 0, 0, 0],
   [1, 1, 0, 0, 0],
   [0, 0, 1, 0, 0],
  [0, 0, 0, 1, 1]
 ]

def solution(grid): 
    ROW = len(grid)
    COL = len(grid[0])
    seen = set()
    count = 0
    
    
    for i in range(ROW):
        for j in range(COL):
            if grid[i][j] == 1:
                count += 1
                dfs(i,j,ROW,COL,seen)
    
    print(count)

def dfs(i,j,ROW,COL,seen):
    if i >= 0 and i < ROW and j >= 0 and j < COL and (i,j) not in seen and grid[i][j] == 1:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        for [p,q] in directions:
            seen.add((p+i, q+j))
            dfs(p+i, q+j,ROW,COL,seen)
                
solution(grid)
