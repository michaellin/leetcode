from typing import *

# Problem:
# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        overflow = 0
            
        if l1.val == 10:
            overflow = 1
            l1.val = 0
        elif l2.val == 10:
            overflow = 1
            l2.val = 0
        
        digit = (l1.val + l2.val)
        if ((digit - 10) >= 0):
            overflow = 1
            digit -= 10
            
        if not l1.next and not l2.next:
            return ListNode(val=digit, next=ListNode(1) if overflow else None)
        if (not l1.next):
            l2.next.val += overflow
            return ListNode(val=digit, next=self.addTwoNumbers(ListNode(0), l2.next))
        elif (not l2.next):
            l1.next.val += overflow
            return ListNode(val=digit, next=self.addTwoNumbers(l1.next, ListNode(0)))
        l1.next.val += overflow
            
        return ListNode(val=digit, next=self.addTwoNumbers(l1.next, l2.next))

s = Solution()
