# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 22:08:15 2023

@author: Seal-Rumi
"""

import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return math.gcd(min(nums), max(nums))