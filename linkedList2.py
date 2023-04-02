# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 22:43:52 2023

@author: priya
"""

class Node: 
    def __init__(self,data):
        self.data = data
        self.next = None
        

head = Node("head")
secondNode = Node("second Node")
thirdNode = Node("third node")
tail = Node("tail")

head.next = secondNode
secondNode.next = thirdNode
thirdNode.next = tail


def printLinkedList(head):
    currentNode = head
    while currentNode != None:
        print(currentNode.data,end= " -> ")
        currentNode = currentNode.next
    print(None)
        
printLinkedList(head)


        
            