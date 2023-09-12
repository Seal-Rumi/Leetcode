# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 22:21:54 2023

@author: Seal-Rumi
"""

class Solution:
    def sumBase(self, n: int, k: int) -> int:
        convert = 0
        temp = n
        while True:
            convert += temp%k
            temp //= k
            if temp == 0:break
        return convert