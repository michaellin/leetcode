from typing import *

import copy

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
      l = [self.val]
      n = self
      while n.next != None:
        n = n.next
        l.append(n.val)
      return str(l)
        

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
      output = ListNode()
      outputPtr = output
      if l1 == None:
        return l2
      elif l2 == None:  
        return l1
      while l1 != None and l2 != None:
        if (l1.val > l2.val):
          outputPtr.next = ListNode(val=l2.val)
          outputPtr = outputPtr.next
          if (l2.next == None):
            outputPtr.next = l1
          l2 = l2.next
        else:
          outputPtr.next = ListNode(val=l1.val)
          outputPtr = outputPtr.next
          if (l1.next == None):
            outputPtr.next = l2
          l1 = l1.next
      output = output.next
      return output
        
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

print(l1)
print(l2)

s = Solution()
print(s.mergeTwoLists(l1, l2))

l2 = ListNode()
print(s.mergeTwoLists(None, l2))
