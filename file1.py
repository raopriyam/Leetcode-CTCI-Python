# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 21:47:56 2023

@author: priya
"""
f = open("try.txt", "a")
f.write("Now the file has more content!")
f.close()


file = open("try.txt", "r")
count = 0

for lines in file:
    if lines != "\n":
            count += 1
    print(lines)

file.close()
print(count) 

