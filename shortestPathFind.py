# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 11:26:33 2023

@author: priya
"""

from collections import deque

class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m,n = len(grid),len(grid[0])
        q = deque([(0,0,k,0)])
        seen = set()
        while q:
            x,y,left,steps = q.popleft()
            if(x,y,left) in seen or left<0:
                continue
            if(x,y) == (m-1,n-1):
                return steps
            seen.add((x,y,left))
            if grid[x][y] == 1:
                left -= 1 
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                new_x, new_y = x+dx, y+dy
                if 0<=new_x<m and 0<=new_y<n:
                    q.append((new_x,new_y,left,steps+1))
        return -1
    
solutionObject = Solution()
print("The steps needed for reaching the end is: ",solutionObject.shortestPath(grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1))