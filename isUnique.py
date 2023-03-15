# -*- coding: utf-8 -*-

def isUnique(string):
    if len(string)>50:
        return False
    elif len(string) != len(set(string)):
        return False
    else:
        return True


print(isUnique("Priyam"))
print(isUnique("Priyamrao"))
            
            
