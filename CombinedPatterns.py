# -*- coding: utf-8 -*-
"""
Created on Thu Nov 20 23:49:44 2025

@author: priya
"""

for i in range(5):
    print("*"*i)
    
for i in range(5):
    print(" "*(i),end="")
    print("*"*(5-i))
    

for i in range(5):
    print("*"*(5-i))
    
for i in range(5):
    print(" "*(5-i),end = "")
    print("*"*i)