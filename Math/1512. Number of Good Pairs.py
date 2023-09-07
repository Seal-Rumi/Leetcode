# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 20:55:48 2023

@author: Seal-Rumi
"""

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        numset = set(nums)
        numcount = [nums.count(i) for i in numset]
        res = 0
        for i in numcount:
            res += i*(i-1)//2
        return res
