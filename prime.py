# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 23:07:54 2023

@author: priya
"""

def prime(n):
    if n>3:
        for i in range(2,int(n/2) + 1):
            if n%i == 0:
                return "not Prime"
        return "Prime"
    elif n==1:
        return "Neither prime nor not prime"
    else:
        return "Prime"
                
    
print(prime(9))