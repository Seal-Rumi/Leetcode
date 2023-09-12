# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 17:16:33 2023

@author: Seal-Rumi
"""

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        xorset = [0]
        for num in nums:
            xorset += [curr^num for curr in xorset]
        output = sum(xorset)
        return output