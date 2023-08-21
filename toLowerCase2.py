# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 23:10:53 2023

@author: priya
"""

def toLowerCase( s):
    """
    :type s: str
    :rtype: str
    """
    ans = ""
    for i in s:
        if ord(i) >= 97 and ord(i) <=122:
            ans = ans + i
        elif ord(i) >= 65 and ord(i) <97:
            ans = ans + chr(ord(i)-32)
        else:
            ans = ans + i
        return ans
    

print(toLowerCase("Priyam Rao"))