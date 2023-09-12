# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 15:28:24 2023

@author: Seal-Rumi
"""

class Solution:
    def maximum69Number (self, num: int) -> int:
        nums = [i for i in str(num)]
        for i in range(len(nums)):
            if nums[i]=='6':
                nums[i]='9'
                break
        return int(''.join(nums))