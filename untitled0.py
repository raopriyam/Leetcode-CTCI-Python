# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 13:00:09 2026

@author: priya
"""

def commonprefix(a,b):
    first,second= str(a), str(b)
    ans = ""
    
    limit = min(len(first),len(second))
    
    for i in range(limit):
        if first[i] != second[i]:
            return len(ans)
        else:
            ans += first[i]
    return len(ans)
                
    

print(commonprefix(12345,293657))
            