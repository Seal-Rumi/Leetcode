# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 17:36:48 2023

@author: Seal-Rumi
"""

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        output = 0
        for i in range(1, len(points)):
            distance = [abs(points[i][0]-points[i-1][0]), abs(points[i][1]-points[i-1][1])]
            step = max(distance)
            output += step
        return output