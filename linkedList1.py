# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 21:46:10 2023

@author: priya
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode
    def printLinkedList(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next
            

firstNode = Node("Priyam")
linkList = LinkedList()
linkList.insert(firstNode)
secondNode = Node("Kaushikbhai")
linkList.insert(secondNode)
thirdNode = Node("Rao")
linkList.insert(thirdNode)
linkList.printLinkedList()

