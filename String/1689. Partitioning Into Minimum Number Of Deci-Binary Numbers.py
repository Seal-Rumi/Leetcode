# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 11:43:56 2023

@author: Seal-Rumi
"""

class Solution:
    def minPartitions(self, n: str) -> int:
        return max([int(i) for i in str(n)])