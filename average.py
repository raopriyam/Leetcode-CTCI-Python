# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 23:01:27 2023

@author: priya
"""

def average(n):
    totalSum = 0
    
    for i in range(n):
        numbers = float(input("enter the number"))
        totalSum += numbers
    return totalSum/n
    
print("Average is ",average(5))