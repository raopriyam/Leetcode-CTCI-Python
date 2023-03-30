# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 22:22:37 2023

@author: priya
"""

def stringRotation(string,n):
    return string[n:] + string[:n]

print(stringRotation("PriyamRao",6))
    