from typing import *
from itertools import combinations

class Solution:
    def combThree(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.explored = set()
        self.combThreeHelper(nums, len(nums), 0, 1, 2, res)
        return res

    def combThreeHelper(self, arr, n, index1, index2, index3, out):
        if (index1, index2, index3) in self.explored:
          return
        if (index1 < index2) and (index2 < index3) and (index3 < n):
            out.append((arr[index1],arr[index2],arr[index3]))
            self.explored.add((index1, index2, index3))
        else:
            return
        #if index1 < (index2 - 1):
        #  self.combThreeHelper(arr, n, index1+1, index2, index3, out)
        if index2 < (index3 - 1):
          self.combThreeHelper(arr, n, index1, index2+1, index3, out)
        if index3 < (n - 1):
          self.combThreeHelper(arr, n, index1, index2, index3+1, out)
          self.combThreeHelper(arr, n, index1, index2+1, index3+1, out)
          self.combThreeHelper(arr, n, index1+1, index2+1, index3+1, out)

s = Solution()
print(s.combThree([-4,-2,1, 0, 0]))
print(len((s.combThree([-4,-2,1, 0, 0]))))
comb = combinations([-4,-2,1, 0, 0], 3)
print(([c for c in comb]))
