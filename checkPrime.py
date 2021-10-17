# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 16:30:21 2021

@author: priya
"""

n = 5
elements = [7,12,13,59,67]
ans = []
def checkPrime(i):
    for j in range(3,int(i/2+1)):
        if i%j == 0:
            return "Composite"
            
        else:
            pass
    return "Prime"
ans = []    
for i in elements:
    ans.append(checkPrime(i))

print(ans)