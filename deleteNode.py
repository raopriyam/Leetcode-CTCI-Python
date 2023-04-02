# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 22:49:50 2023

@author: priya
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
head = Node("head")
secondNode = Node("second node")
tail = Node("tail")

head.next = secondNode
secondNode.next = tail

newNode = Node("new node")

def insertNodeAtTheEnd(head,newNode):
    currentNode = head
    while currentNode.next != None:
        currentNode = currentNode.next
    currentNode.next = newNode
    currentNode.next.next = None
    
def deleteNodeAtTheEnd(head):
    currentNode = head
    while currentNode.next.next != None:
        currentNode = currentNode.next
    currentNode.next = None
    

def printLinkedList(head):
    currentNode = head
    while currentNode != None:
        print(currentNode.data,end = " -> ")
        currentNode = currentNode.next
    print("None")
    
printLinkedList(head)
insertNodeAtTheEnd(head, newNode)
printLinkedList(head)
deleteNodeAtTheEnd(head)
printLinkedList(head)