# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 23:32:55 2023

@author: Seal-Rumi
"""

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')