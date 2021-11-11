# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 22:44:53 2021

@author: priya
"""

def stringprintK(s):
    strn = ""
    j = 0
    for i in range(0,len(s)+1,2):
        if i%4 != 0:
            a = s[j:i]
            strn = strn + a[::-1]
        if i%4 == 0:
            strn = strn + s[j:i]
        j = i
    #strn = strn + s[j:i]
    return strn 

print(stringprintK("abcdefgh"))
        