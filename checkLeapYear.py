# -*- coding: utf-8 -*-
"""
Created on Sun Dec 14 23:51:34 2025

@author: priya
"""

def checkLeapYear(year):
    if year % 4 == 0:
        return True
    
    return False


print(checkLeapYear(1998))