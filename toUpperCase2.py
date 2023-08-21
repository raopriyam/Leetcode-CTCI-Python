# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 23:18:19 2023

@author: priya
"""

def toUpperCase( s):
    """
    :type s: str
    :rtype: str
    """
    ans = ""
    for i in s:
        if ord(i) >= 97 and ord(i) <=122:
            ans = ans + chr(ord(i)-32)
        elif ord(i) >= 65 and ord(i) <97:
            ans = ans + i
        else:
            ans = ans + i
        return ans
    

print(toUpperCase("Priyam Rao"))