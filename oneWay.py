# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 18:09:46 2021

@author: priya
"""

def oneAway(s1,s2):
    count = 0
    if len(s1) == len(s2):
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
    elif len(s1) == len(s2)-1:
        count = 1
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
    elif len(s2) == len(s1)-1:
        count = 1
        for i in range(len(s2)):
            if s1[i] != s2[i]:
                count += 1
                
    else:
        return -1
        
    return count

a = oneAway("Priyam","Priya")
print(a)
if a==0 or a==1:
    print(True)
else:
    print(False)