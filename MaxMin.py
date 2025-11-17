# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 22:53:36 2025

@author: priya
"""

from collections import deque

def maxMin(arr, window_length):
    """
    Returns the maximum among the minima of all subarrays
    (contiguous windows) of length `window_length`.
    Time complexity: O(n)
    """

    n = len(arr)
    if window_length == 0 or n == 0:
        return None  # or raise error depending on problem specs

    # Deque will store indices of elements.
    # It will be maintained so that arr[indices] is increasing.
    index_deque = deque()

    maximum_of_minima = float('-inf')

    for current_index in range(n):
        current_value = arr[current_index]

        # 1. Remove indices that are out of the current window
        while index_deque and index_deque[0] <= current_index - window_length:
            index_deque.popleft()

        # 2. Maintain increasing order in deque
        # Remove indices whose values are >= current_value
        while index_deque and arr[index_deque[-1]] >= current_value:
            index_deque.pop()

        # 3. Add current index
        index_deque.append(current_index)

        # 4. When we've processed the first full window, start recording minima
        if current_index >= window_length - 1:
            window_minimum = arr[index_deque[0]]
            if window_minimum > maximum_of_minima:
                maximum_of_minima = window_minimum

    return maximum_of_minima
