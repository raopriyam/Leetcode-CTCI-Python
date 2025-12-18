# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 23:33:31 2025

@author: priya
"""

def checkPrine(n):
    countFactors = 0
    for i in range(1,int(n/2)+1):
        if n%i == 0:
            countFactors += 1
            
    if countFactors > 1:
        print("Not Prime")
    else:
        print("Prime")
        
checkPrine(27)