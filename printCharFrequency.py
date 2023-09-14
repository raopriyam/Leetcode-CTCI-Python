# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 17:31:07 2023

@author: priya
"""

def printCharFrequency(s):
    ans = ""
    check = 1
    for i in range(1,len(s)):
        if s[i-1] == s[i]:
            check += 1
        else:
            ans = ans + s[i-1] + str(check)
            check = 1
    ans = ans + s[-1] + str(check)
    return ans

print(printCharFrequency("GeeeEEkkks"))
            
        
        