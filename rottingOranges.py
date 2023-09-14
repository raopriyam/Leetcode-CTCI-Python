# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 10:17:59 2023

@author: priya
"""

from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q = deque()
        time = 0
        fresh = 0

        ROWS = len(grid)
        COLS = len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])

        directions = [[0,1],[0,-1], [1,0], [-1,0]]
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if(row < 0 or row == len(grid) or
                        col<0 or col == len(grid[0]) or 
                        grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    q.append([row,col])
                    fresh -= 1
            time += 1
        if fresh == 0:
            return time
        else:
            return -1 
        
solutionObject = Solution()
output = solutionObject.orangesRotting(grid = [[2,1,1],[1,1,0],[0,1,1]])

#use assert statement here to compare the expected output
assert output == 4, "The test case doesn't pass. The output is not equals to expected output."
print("the time required for oranges to become rotten is: ",output)  


