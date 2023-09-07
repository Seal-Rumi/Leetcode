# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 21:53:32 2023

@author: Seal-Rumi
"""

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        digit_sum = 0
        for i in nums:
            temp = [int(j) for j in str(i)]
            digit_sum += sum(temp)
        element_sum = sum(nums)
        return abs(element_sum-digit_sum)