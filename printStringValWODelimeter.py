# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 17:37:06 2023

@author: priya
"""

def printStringValWODelimeter(listString):
    temp = "".join(listString)
    temp = temp[:len(temp)-1] if temp[-1] == "$" else temp
    return temp.split("$")

print(printStringValWODelimeter(["one$","two$three$", "four","Five","six$","seven$"]))