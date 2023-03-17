# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 22:26:15 2023

@author: priya
"""

def oneAway(firstString, secondString):
    if len(firstString) > len(secondString):
        if len(firstString) - len(secondString) > 1:
            return False
        
        check = 0
        
        for i in firstString:
            if i not in secondString:
                check = check + 1 
                
        return check == 1
    
    else:
        if len(secondString) - len(firstString) > 1:
            return False
        
        check = 0
        
        for i in secondString:
            if i not in firstString:
                check = check + 1 
                
        return check == 1

print(oneAway("priyam", "priyams"))