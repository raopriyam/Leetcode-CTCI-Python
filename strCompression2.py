# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 23:15:48 2022

@author: priya
"""

def strCompress(s):
    count = 1
    result = ""
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count = count + 1
        else:
            result = result +  s[i] + str(count)
            count = 1
    result = result +  s[i+1] + str(count)
    return result
        
        
        
print(strCompress("aaabcccccaaaaaa"))