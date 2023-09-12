# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 15:55:59 2023

@author: Seal-Rumi
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        count = 0
        numlist = []
        while True:
            numlist.append(head.val)
            head = head.next
            if head==None:break
        output = 0
        for i in numlist:
            output<<=1
            output+=i
        return output