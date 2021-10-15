# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 22:18:02 2021

@author: priya
"""
ls = [1,2,3,4,5,2,4,2,2,4,5,3,2,1,2,5,4,3,6,5,3,4,0]
dict1 = {}
ans = []
for i in ls:
    if i not in dict1:
        ans.append(i)
        dict1[i] =1

print(ans)
        
    
    