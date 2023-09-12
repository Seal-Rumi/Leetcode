# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 21:53:04 2023

@author: Seal-Rumi
"""

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        reverse = str(int(str(num)[::-1]))
        return len(reverse)==len(str(num))