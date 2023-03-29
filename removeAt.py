# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 22:25:47 2023

@author: priya
"""

def remove_at(input_string, index):
    before_index = input_string[:index:]
    after_index  =input_string[index+1::]
    return before_index + after_index


string = 'python'
index = int(input("Enter the index to remove the character"))
print(remove_at(string,index))                                                                          
