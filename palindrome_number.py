# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 22:08:36 2022

@author: priya
"""

def palindrome(n):
    if n<0:
        return False
    else:
        a1 = str(n)
        a2 = a1[::-1]
        return a1==a2
    

print(palindrome(123))

print(palindrome(121))

print(palindrome(1221))

print(palindrome(12321))

print(palindrome(0))