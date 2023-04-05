# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 22:04:29 2023

@author: priya
"""

def are_anagrams(str1, str2):
    # Convert the strings to lowercase and remove whitespaces
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    
    # If the length of the two strings are different, they are not anagrams
    if len(str1) != len(str2):
        return False
    
    # Convert the strings to lists and sort them
    str1_list = sorted(list(str1))
    str2_list = sorted(list(str2))
    
    # Compare the two sorted lists
    if str1_list == str2_list:
        return True
    else:
        return False


print(are_anagrams("priyam", "mapyir"))