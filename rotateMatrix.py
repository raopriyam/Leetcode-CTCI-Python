# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 18:24:45 2021

@author: priya
"""

def zeroMatrix(matrix):
    print(matrix)
    if matrix:
        rowlen = len(matrix)
        collen = len(matrix[0])
        left = 0
        right = rowlen-1
        while left<right:
            temp = matrix[left]
            matrix[left] = matrix[right]
            matrix[right] = temp
            left += 1
            right -= 1
            
        
        for i in range(rowlen):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        
            
        
        
            
            
        print(matrix)
        

zeroMatrix([[1,2,3],[4,5,6],[7,8,9]])