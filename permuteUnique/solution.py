from typing import *

from collections import Counter
import copy

# Problem:
# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        out = []
        counter = Counter(nums) 
        self.permuteUniqueRecursive(counter, [], out)
        return out

    def permuteUniqueRecursive(self, counter, listSofar, out):
        if (sum(counter.values()) == 0):
          out.append(listSofar)
        for e, n in counter.items():
          if n > 0:
            newCounter = counter.copy()
            newCounter[e] -= 1
            newListSofar = copy.deepcopy(listSofar)
            newListSofar.append(e)
            self.permuteUniqueRecursive(newCounter, newListSofar, out)
        
s = Solution()
print(s.permuteUnique([]))
print(s.permuteUnique([1]))
print(s.permuteUnique([1,2]))
print(s.permuteUnique([1,40,30,20,10,50]))
