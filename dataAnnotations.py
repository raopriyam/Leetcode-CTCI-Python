# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 17:41:28 2024

@author: priya
"""

def decode(message_file):
    message = []
    
    with open(message_file, 'r') as file:
        lines = file.readlines()
        dictionary = {}
        
        for line in lines:
            splitLine = line.split(' ')
            dictionary[splitLine[0]] = splitLine[1].strip()
        
        numOfLines = len(lines)
        pyramid = []
        i = 1
        j = 1
        while i <= numOfLines:
            temp = []
            k = j
            while k > 0:
                k -= 1
                temp.append(i)
                i += 1
            j += 1
            pyramid.append(temp)
        print(pyramid)

        for i in range(len(pyramid)):
            message.append(dictionary[str(pyramid[i][-1])])
    
    return ' '.join(message)


decoded_message = decode("message.txt")
print(decoded_message)