# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 23:26:06 2023

@author: priya
"""

def fibo1(n):
    n1 = 0
    n2 = 1
    print(n1," ",n2, end = " ")
    n3 = n2 + n1
    for i in range(2,n):
        print(" ",n3, end = " ")
        temp = n3
        n3 = n2 + n3
        n2 = temp
        
fibo1(5)
        
        
        