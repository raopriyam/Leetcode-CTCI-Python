# -*- coding: utf-8 -*-

def Urlify(string):
    ans = ""
    for i in string:
        if i == " ":
            ans = ans + "%"
        else: 
            ans = ans + i
    return ans
        

print(Urlify("priyam Rao"))
