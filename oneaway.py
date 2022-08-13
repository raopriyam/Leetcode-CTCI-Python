# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 18:43:33 2022

@author: priya
"""

def oneaway(s1,s2):
    n1 = len(s1)
    n2 = len(s2)
    check = 0
    if (max(n1,n2)-min(n1,n2))>1:
        return False
    else:
        set1 = set(s1)
        for i in s2:
            if i not in set1:
                check = check+1
    if check >1:
        return False
    else:
        return True
    
print(oneaway("ple","pales"))
    
    