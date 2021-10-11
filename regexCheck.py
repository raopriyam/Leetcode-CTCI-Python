# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 18:32:47 2021

@author: priya
"""

import re
 
# the regular  expression
regex = r'^[a-z]$|^([a-z]).*\1$'
 
# function for checking the string
def check(string):
 
    # pass the regular expression
    # and the string in the search() method
    if(re.search(regex, string)): 
        print("Valid") 
    else: 
        print("Invalid") 
 
if __name__ == '__main__' :
 
    sample1 = "abba"
    sample2 = "a"
    sample3 = "abcd"
    sample4 = "abbcda"
 
    check(sample1)
    check(sample2)
    check(sample3)
    check(sample4)