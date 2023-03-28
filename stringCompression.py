# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 22:32:21 2023

@author: priya
"""

def stringCompression(string):
    compressed = ""
    count = 1
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            count +=1 
        else:
            compressed = compressed + string[i] + str(count)
            count = 1
    compressed = compressed + string[i]+ str(i)
    
    if len(string) <= len(compressed):
        return string
    else:
        return compressed
    
print(stringCompression("aabccccaaa"))
print(stringCompression("aaaaaabbccbcaabb"))