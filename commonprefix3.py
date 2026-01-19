# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 03:20:25 2026

@author: priya
"""

def commonprefix3(arr1,arr2):
    best = 0
    set1 = set()
    
    for i in arr1:
        s1 = str(i)
        for j in range(1,len(s1)+1):
            set1.add(s1[:j])
    #print(set1)
    
    for i in arr2:
        s2 = str(i)
        for j in range(1,len(s2)+1):
            if s2[:j] in set1:
                best = max(best,j) 
    return best
    
print(commonprefix3([123,12,12645], [1,23,1234]))