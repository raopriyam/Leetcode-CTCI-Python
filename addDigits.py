# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 22:34:38 2022

@author: priya
"""

def addDigits(num):
    """
    :type num: int
    :rtype: int
    """
    def breakAndAdd(n):
        sum1 = 0
        n1 = str(n)
        for i in n1:
            sum1 = sum1+int(i)
        return sum1
    while num>9:
        num = breakAndAdd(num)
    return num

print(addDigits(38))