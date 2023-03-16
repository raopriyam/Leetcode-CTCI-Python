# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 20:44:44 2023

@author: priya
"""

def normalize(string):
    string = string.replace(" ","")
    return string.lower()

print(normalize("Priyam Rao"))
print(normalize("This is Normalize Function"))