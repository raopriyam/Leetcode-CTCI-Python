# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 20:32:38 2022

@author: priya
"""

def sobotragammaticStings(n):
        #no upside down options
    if '2' in n or '3' in n or '4' in n or '5' in n or '7' in n:
        return False
    
    n2 = '' #our comparision string
    for i in n:
        #swap 6s and 9s
        if i == '6':
            n2 += '9'
        elif i == '9':
            n2 += '6'
        
        else: #leave 1s and 8 alone
            n2 += i
    
    #reverse it at the end and compare
    return n2[::-1]==n 

print(sobotragammaticStings("1961"))