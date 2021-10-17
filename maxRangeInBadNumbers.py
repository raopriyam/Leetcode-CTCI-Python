# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 17:38:10 2021

@author: priya
"""

low = 300
upper = 1000
temp = 0
sum1 = 0
i = 0
badNumbers = [7,90,100,541,653,769,876,987]
while i<len(badNumbers)-1:
    if low>badNumbers[i]:
        i = i+1
        continue
    sum1 = badNumbers[i+1]-badNumbers[i]
    temp = max(temp,sum1)
    i = i+1
    
print(temp)
    