# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 23:02:27 2023

@author: priya
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
head = Node("head")
secondNode = Node("second node")
thirdNode = Node("third node")
fourthNode = Node("fourth node")
tail = Node("tail")

head.next = secondNode
secondNode.next = thirdNode
thirdNode.next = fourthNode
fourthNode.next = tail

def reverseLinkedList(head):
    currentNode = head
    previousNode = None
    while currentNode != None:
        nextNode = currentNode.next
        currentNode.next = previousNode
        previousNode = currentNode
        currentNode = nextNode
        
def printLinkedList(head):
    currentNode = head
    while currentNode != None:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("None")
    
    
printLinkedList(head)
reverseLinkedList(head)
printLinkedList(tail)