# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 12:19:11 2021

@author: priya
"""

"Is unique string: All the characters in the string must be unique"

def isUnique1(str):
    for i in range(len(str)):
        for j in range(i+1,len(str)):
            if str[i] == str[j]:
                return False
    return True

print("Brute force")

print(isUnique1("priyam"))
print(isUnique1("priyrm"))
print(isUnique1("priyamrao"))
print(isUnique1("raoRAO"))
print()


def isUnique2(str):
    ls = list(str)
    ls.sort()
    for i in range(1,len(ls)):
        if ls[i-1] == ls[i]:
            return False
    return True

print("sort and compare")

print(isUnique2("priyam"))
print(isUnique2("priyrm"))
print(isUnique2("priyamrao"))
print(isUnique2("raoRAO"))
print()



def isUnique3(str):
    dic = {}
    count = 0
    for i in str:
        if i in dic:
            return False
        else:
            dic[i] = count 
            count += 1
    return True
        
print("dictionatry")

print(isUnique3("priyam"))
print(isUnique3("priyrm"))
print(isUnique3("priyamrao"))
print(isUnique3("raoRAO"))
print()



def isUnique4(str):
    if len(str) >128:
        return False
    else:
        bul = [False] * 128
        for i in str:
            ind = ord(i)
            if bul[ind]:
                return False
            else:
                bul[ind] = True
        return True
    
print("boolean array")

print(isUnique4("priyam"))
print(isUnique4("priyrm"))
print(isUnique4("priyamrao"))
print(isUnique4("raoRAO"))
print()
    




