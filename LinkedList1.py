# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 21:42:28 2022

@author: priya
"""

class LinkedListNode:
    def __init__(self,value,nextNode = None):
        self.value = value
        self.nextNode = nextNode
        
node1 = LinkedListNode(1)
node2 = LinkedListNode(2)
node3 = LinkedListNode(3)
node4 = LinkedListNode(4)
node5 = LinkedListNode(5)    

node1.nextNode = node2 
node2.nextNode = node3
node3.nextNode = node4
node4.nextNode = node5

curr = node1
while True:
    print(curr.value,"->",end = " ")
    if curr.nextNode is None:
        print(None)
        break
    curr = curr.nextNode
    