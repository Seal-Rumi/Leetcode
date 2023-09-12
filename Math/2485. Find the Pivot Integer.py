# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 23:09:16 2023

@author: Seal-Rumi
"""

class Solution:
    def pivotInteger(self, n: int) -> int:
        nums = [i for i in range(1, n+1)]+[0]
        for i in range(1, n+1):
            if sum(nums[:i])==sum(nums[i-1:]):
                return i
        return -1