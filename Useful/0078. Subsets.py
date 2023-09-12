# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 16:10:09 2023

@author: Seal-Rumi
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        for num in nums:
                output += [curr + [num] for curr in output]
        return output