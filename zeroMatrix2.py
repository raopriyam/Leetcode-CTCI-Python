# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 21:39:30 2022

@author: priya
"""

def zeroMatrix(mat):
    colnum = []
    rownum = []
    rowlen = len(mat)
    collen = len(mat[0])
    for i in range(rowlen):
        for j in range(collen):
            if mat[i][j] == 0:
                rownum.append(i)
                colnum.append(j)
                
    for i in rownum:
        mat[i] = [0]*collen
        
    for i in mat:
        for j in colnum:
            i[j] = 0
            
    return mat 

print(zeroMatrix([[1,2,3],[4,0,6],[7,8,9]]))
            