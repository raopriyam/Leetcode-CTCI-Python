# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 03:39:43 2026

@author: priya
"""

def commonprefix(a,b):
    s1,s2 = str(a),str(b)
    limit = min(len(s1),len(s2))
    count = 0
    
    for i in range(limit):
        if s1[i] != s2[i]:
            return count
        count += 1
    return count

print(commonprefix(123, 1243))


def commonprefix2(a,arr1):
    s1 = str(a)
    best = 0
    for i in arr1:
        s2 = str(i)
        count = 0
        
        limit = min(len(s1),len(s2))
        for j in range(limit):
            if s2[j] != s1[j]:
                break
            count += 1
        best = max(count,best)
    
    return best


def commonprefix3(arr1,arr2):
    prefixset = set()
    
    for i in arr1:
        s1 = str(i)
        for j in range(1,len(s1)+1):
            prefixset.add(s1[:j])
            
    best = 0
    
    for i in arr2:
        s2 = str(i)
        for j in range(1,len(s2)+1):
            if s2[:j] in prefixset:
                best = max(best,j)
                
    return best