# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 21:32:33 2023

@author: Seal-Rumi
"""

class Solution:
    def minimumSum(self, num: int) -> int:
        nums = [int(i) for i in str(num)]
        nums.sort()
        return 10*(nums[0]+nums[1])+nums[2]+nums[3]