from typing import *
from itertools import combinations



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        combs = combinations(nums, 3)
        res = []
        visited = []
        for c in combs:
            if (sum(c) == 0):
                if (Counter(c) not in visited):
                  res.append(c)
                  visited.append(Counter(c))
        return res

s = Solution()
#print(s.sameElems([1,2,1],[2,1,0]))
#print(s.threeSum([-1,0,1,2,-1,-4]))
print(s.threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]))

#print(s.sameElems((4,-4,0),(0,0,0)))
