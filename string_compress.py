# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 20:41:05 2023

@author: priya
"""

def string_comp(s):
    scomp = [s[0]]
    count = 1
    
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            scomp.extend([count,s[i]])
            count = 1
    scomp.append(count)
    
    res = ''.join(map(str, scomp))
    
    return res

s = "aaabbcccddeee"
    
c_string = string_comp(s)

if len(c_string) < len(s):
    print(c_string)
else:
    print(s)
    


