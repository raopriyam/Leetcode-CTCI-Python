# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 22:18:48 2023

@author: priya
"""

def oneAwaySameLength(s1,s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1 
            if count>1:
                return False
    return True

def oneAwayDiffLength(s1,s2):
    j = count = i = 0
    while i<len(s2):
        if s2[i] == s1[j]:
            i += 1
            j += 1 
        else: 
            j += 1 
            count += 1
            if count > 1:
                return False
    return True
            
        

def oneAway(s1,s2):
    if abs(len(s1)-len(s2)>1):
        return False
    elif len(s1) == len(s2):
        return oneAwaySameLength(s1,s2)
    elif len(s1) > len(s2):
        return oneAwayDiffLength(s1,s2)
    elif len(s1) < len(s2):
        return oneAwayDiffLength(s2,s1)
    else:
        return ("invalid")
    
print(oneAway("stringy","strung"))