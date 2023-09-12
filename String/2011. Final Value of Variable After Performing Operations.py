# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 23:36:09 2023

@author: Seal-Rumi
"""

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for i in operations:
            if i == "++X" or i == "X++":
                x += 1
            if i == "--X" or i == "X--":
                x -= 1
        return x