# -*- coding: utf-8 -*-
"""
Created on Sun Feb  8 20:01:43 2026

@author: priya
"""

def detectCapitalUse(self, word: str) -> bool:
    option1 = word.upper()
    option2 = word.lower()
    option3 = ""
    option3 = word[0].upper() + word[1:].lower()

    return (word == option1 or word == option2 or word == option3)
     