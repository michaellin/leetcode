from typing import *
# Problem:
# Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.
# Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while (i < len(nums)):
            currElem = nums[i]
            elemCount, elemIdx = 1, i + 1
            while (elemIdx < len(nums)) and (nums[elemIdx] == currElem):
              elemCount += 1
              elemIdx += 1
            #get how many to pop
            numPop = elemCount-2
            [nums.pop(i) for x in range(numPop) if numPop > 0]
            i += 2 if numPop > 0 else elemCount

        return len(nums)
        
s = Solution()
print(s.removeDuplicates([1,2,3,4,4]))
print(s.removeDuplicates([1,1,1,2,2,3]))
print(s.removeDuplicates([0,0,1,1,1,1,2,3,3]))

