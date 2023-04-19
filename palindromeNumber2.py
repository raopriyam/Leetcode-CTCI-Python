# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 21:56:19 2023

@author: priya
"""

def palindromeNumber2(number):
    check = number
    sum = 0
    while number > 0:
        r = number % 10
        sum = sum*10 + r
        number = int(number/10)
    return sum == check

print(palindromeNumber2(12321))