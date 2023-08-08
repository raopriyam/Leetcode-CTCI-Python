# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 22:36:18 2023

@author: priya
"""

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x<0:
        return False
    elif x<10:
        return True
    else:
        check = x
        sum1 = 0
        while x>0:
            r = x%10
            sum1 = sum1*10 + r
            x = x/10
    print(sum1,check)
    return check == sum1

print(isPalindrome(121))