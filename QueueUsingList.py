# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 22:22:29 2021

@author: priya
"""

queue = []


def removeFromQueue():
    if queue:
        queue.pop(0)
    else:
        print("empty Queue")
    
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)


removeFromQueue()
print(queue)

removeFromQueue()
print(queue)

removeFromQueue()
print(queue)

removeFromQueue()
print(queue)

removeFromQueue()
print(queue)

removeFromQueue()
print(queue)