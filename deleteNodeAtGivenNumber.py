# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 22:01:18 2023

@author: priya
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
head = Node("head")
secondNode = Node("second node")
thirdNode = Node("third node")

newNode = Node("new node")
middleNode = Node("middle node")

head.next = secondNode
secondNode.next = thirdNode
        
def printLinkedList(head):
    currentNode = head
    while currentNode!= None:
        print(currentNode.data,end=" -> ")
        currentNode = currentNode.next
    print("None")
    
    
def insertNodeAtTheEnd(head,newNode):
    currentNode = head
    while currentNode.next != None:
        currentNode = currentNode.next
    currentNode.next = newNode
    newNode.next = None
    
def deleteNodeAtTheEnd(head):
    currentNode = head
    while currentNode.next.next != None:
        currentNode = currentNode.next
    currentNode.next = None
    
def linkedListLength(head):
    currentNode = head
    count = 0
    while currentNode != None:
        currentNode = currentNode.next
        count += 1
    return count

def deleteNodeAtGivenNumber(head,n):
    currentNode = head
    nextNode = currentNode.next
    count = 1
    while count < n-1:
        currentNode = currentNode.next
        nextNode = currentNode.next
        count += 1
    nextNode = nextNode.next
    currentNode.next = nextNode
    
    
printLinkedList(head)
print(linkedListLength(head))
insertNodeAtTheEnd(head, newNode)
printLinkedList(head)
print(linkedListLength(head))
deleteNodeAtTheEnd(head)
printLinkedList(head)
print(linkedListLength(head))
insertNodeAtTheEnd(head, newNode)
deleteNodeAtGivenNumber(head, 3) 
printLinkedList(head)
print(linkedListLength(head))
