# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 23:10:34 2023

@author: priya
"""

def leapYear(year):
    if year%4 == 0:
        return "Leap Year"
    return "Not a Leap Year"

print(leapYear(2020))