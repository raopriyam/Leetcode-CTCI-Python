# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 23:21:30 2023

@author: priya
"""

def prime2(n):
    if n>3:
        for i in range(2,n):
            if n%i == 0:
                return "not Prime"
        return "Prime"
    elif n==1:
        return "Neither prime nor not prime"
    else:
        return "Prime"
                

print(prime2(9))