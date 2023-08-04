# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 22:36:35 2023

@author: priya
"""

def defangIPaddr(address):
    """
    :type address: str
    :rtype: str
    """
    ans = ""
    leng = len(address)
    for i in range(leng):
        if address[i] == ".":
            ans = ans + "[" + address[i] + "]"
        else:
            ans = ans + address[i]
    return ans

print(defangIPaddr("1.1.1.1"))