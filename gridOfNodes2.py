# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 13:21:35 2021

@author: priya
"""

def gridOfNodes(grid):
    ans = 0
    last = 0
    for i in grid:
        count = i.count(1)
        if count>0:
            ans = ans + last*count 
            last =count
    return ans


print(gridOfNodes([[1,1,1],[0,1,0],[0,0,0],[1,1,0]]))