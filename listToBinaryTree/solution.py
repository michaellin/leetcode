from typing import *

# Problem:
# Return the root node of a binary search tree that matches the given preorder traversal.
# (Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, 
# and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)
# It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        queue = []
        out = [self.val]
  
        queue.append(self.left)
        queue.append(self.right)
        while (len(queue) > 0):
          node = queue.pop(0)
          if (node != None):
            out.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
          else:
            out.append(None)

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        pass
        


s = Solution()
