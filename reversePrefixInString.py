# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 09:25:52 2026

@author: priya
"""

def reversePrefix(self, s: str, k: int) -> str:
    return s[0:k][::-1] + s[k:]
    