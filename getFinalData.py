# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 22:51:36 2025

@author: priya
"""

def getFinalData(initial_data, updates):
    n = len(initial_data)
    
    # Step 1: Build difference array for flip counting
    flip_effect = [0] * (n + 1)

    for left, right in updates:
        # Convert 1-based to 0-based
        left -= 1
        right -= 1

        flip_effect[left] += 1
        if right + 1 < n:
            flip_effect[right + 1] -= 1

    # Step 2: Convert difference array to actual flip counts
    flip_count = [0] * n
    running_flips = 0
    for i in range(n):
        running_flips += flip_effect[i]
        flip_count[i] = running_flips

    # Step 3: Apply negations based on odd/even flips
    final_data = []
    for i in range(n):
        if flip_count[i] % 2 == 1:
            final_data.append(-initial_data[i])
        else:
            final_data.append(initial_data[i])

    return final_data
