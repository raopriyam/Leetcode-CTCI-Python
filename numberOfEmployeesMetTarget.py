# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 22:10:22 2023

@author: priya
"""

def numberOfEmployeesWhoMetTarget(hours, target):
    """
    :type hours: List[int]
    :type target: int
    :rtype: int
    """
    check = 0
    for i in hours:
        if i>= target:
            check += 1
    return check

print(numberOfEmployeesWhoMetTarget(hours = [0,1,2,3,4], target = 2))