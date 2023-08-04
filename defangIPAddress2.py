# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 22:37:57 2023

@author: priya
"""

def defangIPaddr(address):
    """
    :type address: str
    :rtype: str
    """
    ans = ""
    for i in address:
        if i == ".":
            ans = ans + "[" + i + "]"
        else:
            ans = ans + i
    return ans

print(defangIPaddr("1.1.1.1"))