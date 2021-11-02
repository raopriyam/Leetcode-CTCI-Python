# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 23:22:46 2021

@author: priya
"""

dict1 = {}
 
# Insert first triplet in dictionary
x, y, z = 10, 20, 30
dict1[x, y, z] = x + y - z;
 
# Insert second triplet in dictionary
x, y, z = 5, 2, 4
dict1[x, y, z] = x + y - z;
 
# print the dictionary
print(dict1)