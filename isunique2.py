# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 13:00:16 2021

@author: priya
"""

def check(s):
    check1 = {}
    count = 0
    for i in s:
        if i not in check1:
            check1[i] = count 
        else:
            return False
        count = count + 1
    return True


print(check("PRIYAM"))
print(check("PRIYAMRAO"))
print(check("PRIyamr"))
print(check("PRIYAMrao"))



print()
print()

def check2(s):
    ans = [True]*128
    if len(s)>128:
        return False
    else:
        for i in s:
            a = ord(i)
            if ans[a] == False:
                return False
            else:
                ans[a]=False
    return True

print(check2("PRIYAM"))
print(check2("PRIYAMRAO"))
print(check2("PRIyamr"))
print(check2("PRIYAMrao"))
        
    