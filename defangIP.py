# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 21:53:57 2022

@author: priya
"""

def defangIP(address):
        newAddress = ""
        for i in address:
            if i == ".":
                newAddress = newAddress + "[" + i + "]"
            else:
                newAddress = newAddress + i
        return newAddress
    
print(defangIP("1.1.1.1"))