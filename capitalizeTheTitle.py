# -*- coding: utf-8 -*-
"""
Created on Sun Feb  8 20:15:58 2026

@author: priya
"""

def capitalizeTitle(self, title: str) -> str:
    list1 = title.split()
    ans = []
    for i in list1:
        if len(i) > 2:
            ans.append(i[0].upper() + i[1:].lower())
        else:
            ans.append(i.lower())
            
    return " ".join(ans)