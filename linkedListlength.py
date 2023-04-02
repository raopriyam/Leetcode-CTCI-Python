# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 22:59:55 2023

@author: priya
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
head = Node("head")
secondNode = Node("second node")
tail = Node("tail")

newNode = Node("new node")

head.next = secondNode
secondNode.next = tail

def printLinkedList(head):
    currentNode = head
    while currentNode != None:
        print(currentNode.data,end= " -> ")
        currentNode = currentNode.next
    print("None")
    
def insertNodeAtTheEndLinkedList(head,newNode):
    currentNode = head
    while currentNode.next != None:
        currentNode = currentNode.next
    currentNode.next = newNode
    currentNode.next.next = None
    
def deleteNodeAtTheEndLinkedList(head):
    currentNode = head
    while currentNode.next.next !=None:
        currentNode = currentNode.next
    currentNode.next = None
    
def LinkedListLength(head):
    currentNode = head
    count = 0
    while currentNode !=None:
        currentNode = currentNode.next
        count += 1
    return count
    
    

printLinkedList(head)
print(LinkedListLength(head))
insertNodeAtTheEndLinkedList(head, newNode)
printLinkedList(head)
print(LinkedListLength(head))
deleteNodeAtTheEndLinkedList(head)
printLinkedList(head)
print(LinkedListLength(head))
