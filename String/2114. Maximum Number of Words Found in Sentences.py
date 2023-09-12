# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 11:49:24 2023

@author: Seal-Rumi
"""

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        n = [len(i.split(" ")) for i in sentences]
        return max(n)