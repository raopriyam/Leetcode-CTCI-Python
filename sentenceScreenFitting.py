# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 22:49:17 2023

@author: priya
"""

class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        total_s = ' '.join(sentence) + ' '
        total_l = len(total_s)
        pointer = 0
        # O(num_of_rows)
        for _ in range(rows):
            pointer += cols
            if total_s[pointer % total_l] == ' ':
                # move to next new position
                pointer += 1
            else:
                # O(max_len_of_word_in_sentence)
                # find the previous space
                while pointer >= 0 and total_s[pointer % total_l] != ' ':
                    pointer -= 1
                # move to next new position
                pointer += 1
        
        return pointer // total_l