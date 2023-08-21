# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 23:25:29 2023

@author: priya
"""

def capitalizeTitle(title):
    """
    :type title: str
    :rtype: str
    """
    check = title.split(" ")
    ans = ""
    for i in check:
        if len(i)<= 2:
            ans = ans + i.lower() + " "
        else:
            ans = ans + i[0].upper() + i[1:].lower() + " "
    return ans[:len(ans)-1]

print(capitalizeTitle("My name is priyam Rao"))