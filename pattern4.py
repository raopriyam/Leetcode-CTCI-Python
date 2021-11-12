# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 23:30:09 2021

@author: priya
"""

def pattern4(n):
    for i in range(1,n+1):
        for j in range(i):
            if (i+j)%2==0:
                print("*",end=" ")
            else:
                print("",end =" ")
        print()

pattern4(10)