# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 21:57:02 2023

@author: priya
"""

def addDigits(num):
    """
    :type num: int
    :rtype: int
    """
    ans = 0
    if num<10:
        return num
    else:
        while num >= 10:
            check = [int(i) for i in str(num)]
            print(check)
            ans = sum(check)
            num = ans
    return ans

print(addDigits(38))