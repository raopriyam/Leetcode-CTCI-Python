# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 16:05:05 2023

@author: priya
"""

filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
