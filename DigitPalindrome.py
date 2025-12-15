# -*- coding: utf-8 -*-
"""
Created on Sun Dec 14 23:34:22 2025

@author: priya
"""

def DigitPalindrome(n):
    sum1 = 0
    check = n
    while n > 0:
        r = n % 10
        sum1 = sum1*10 + r
        n = int(n/10)
    return sum1 == check


print(DigitPalindrome(123211))        
        
        