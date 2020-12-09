from typing import *
from itertools import combinations



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        combs = combinations(nums, 3)
        res = []
        for c in combs:
            if (sum(c) == 0):
                contained = False
                for r in res:
                    if self.sameElems(r, c):
                        contained = True
                if not contained: res.append(c)
        return res

    def sameElems(self, arr1, arr2):
        explore = 3*[False]
        for a in arr1:
            for i in range(len(arr2)):
                if a == arr2[i] and not explore[i]:
                    explore[i] = True
                    break
        return all(explore)

s = Solution()
#print(s.sameElems([1,2,1],[2,1,0]))
#print(s.threeSum([-1,0,1,2,-1,-4]))
print(s.threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]))

#print(s.sameElems((4,-4,0),(0,0,0)))
