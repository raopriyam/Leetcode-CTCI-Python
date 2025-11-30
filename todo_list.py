# -*- coding: utf-8 -*-
"""
Created on Sat Nov 29 23:01:46 2025

@author: priya
"""
todo_list = []

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")
        todo_list.append(task)
        print("Task added!")
    elif choice == "2":
        print("\nYour Tasks:")
        for i, t in enumerate(todo_list, 1):
            print(i, t)
    elif choice == "3":
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(todo_list):
            todo_list.pop(num - 1)
            print("Task removed!")
        else:
            print("Invalid number!")
    elif choice == "4":
        break
    else:
        print("Invalid choice!")

