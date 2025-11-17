# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 00:37:29 2025

@author: priya
"""

def DataUpdate(data,updates):
    if not data:
        return None
    
    if not updates:
        return data
    
    for i in updates:
        for j in range(i[0]-1,i[1]):
            data[j] = data[j]*(-1)
            
    return data


print(DataUpdate([3, 1, 3, 0, 7],[[1, 4], [3, 5], [1, 4], [3, 5], [2, 3]]))