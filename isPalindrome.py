# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 22:33:43 2023

@author: priya
"""

def isPalindrome( x):
    """
    :type x: int
    :rtype: bool
    """
    if x<0:
        return False
    elif x<10:
        return True
    else:
        return str(x) == str(x)[::-1]

print(isPalindrome(121))