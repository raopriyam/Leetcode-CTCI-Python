# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 09:25:18 2026

@author: priya
"""

def reverseStr(self, s: str, k: int) -> str:
    ans = []
    for i in range(0,len(s), 2*k):
        ans.append(s[i:i+k][::-1])
        ans.append(s[i+k:i+2*k])

    return "".join(ans)
