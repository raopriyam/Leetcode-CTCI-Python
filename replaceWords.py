# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 21:54:56 2021

@author: priya
"""

def replaceWords(dictionary,sentence):
    sent = sentence.split(" ")
    dictionary.sort()
    for i in range(len(sent)):
        for root in dictionary:
            if len(root)==1:
                n = 1
            else:
                n = len(root)
            if root[:n] == sent[i][:n]:
                sent[i] =root
                break
    return " ".join(sent)

print(replaceWords(["cat","bat","rat"],"the cattle was rattled by the battery"))
print(replaceWords(["a","b","c"],"aadsfasf absbs bbab cadsfafs"))