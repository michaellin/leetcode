from typing import *

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if (len(nums1) == 0 and len(nums2) == 0):
          return None
        odd1 = len(nums1) % 2
        odd2 = len(nums2) % 2
        oddBoth = (len(nums1) + len(nums2)) % 2

        partitionMiddle = (len(nums1) + len(nums2) + 1)//2
        
        medianNums1Idx = len(nums1)//2

        highIdx = len(nums1)
        lowIdx = 0
        # perform binary search for correct partition
        while (lowIdx <= highIdx):
            # search where to partition
            partIdx1 = (lowIdx + highIdx + 1)//2 # round up
            partIdx2 = (len(nums2) - partIdx1 - 1) if partIdx1 < partitionMiddle else (len(nums1) - partIdx1)
            
            if (partIdx2 < (len(nums2)-1) and partIdx2 >= 0):
              valLeft1 = nums1[partIdx1]
              valRight1 = nums1[partIdx1 + 1]
              partIdx2 =  
            if (lowIdx == (len(sortedList))):
                return (len(sortedList))
            if (highIdx == 0):
                return 0
            leftVal = sortedList[mid_idx-1]
            rightVal = sortedList[mid_idx]
            
            if (leftVal <= val and val <= rightVal): # found location
                return mid_idx
            
            if (leftVal > val):
                high = mid_idx - 1
            elif (val > rightVal):
                low = mid_idx + 1
        
        return low




        # binary search on nums2
        insertIdx = self.binarySearchInsertIdx(medianNums1, nums2)
        medianNums1Idx += 1
        medianNums2Idx = insertIdx
        
        # how many elements to the right and to the left
        right_elems = len(nums2) - insertIdx
        left_elems = insert_idx
        
        med_res = med_nums1
        # if all nums odd then search until left and right are equal
        if (m_n_odd):
            while (right_elems != left_elems):
              if (right_elems > left_elems):
                if (nums1[medianNums1Idx] <= nums2[mediansNums2Idx]):
                  med_res = nums1[medianNums1Idx]
                  medianNums1Idx += 1
                else:
                  med_res = nums2[medianNums2Idx]
                  medianNums2Idx += 1
              else:
                if (nums1[medianNums1Idx] <= nums2[mediansNums2Idx]):
                  med_res = nums1[medianNums1Idx]
                  medianNums1Idx += 1
                else:
                  med_res = nums2[medianNums2Idx]
                  medianNums2Idx += 1
        # if all nums even then search until left larger than right by 1
        else:
            
        
    def binarySearchInsertIdx(self, val: int, sortedList: List[int]) -> int:
        # search index at which value would be inserted
        high = len(sortedList)
        low = 0
        while (low <= high):
            mid_idx = (low + high + 1)//2 # round up
            
            if (low == (len(sortedList))):
                return (len(sortedList))
            if (high == 0):
                return 0
            leftVal = sortedList[mid_idx-1]
            rightVal = sortedList[mid_idx]
            
            if (leftVal <= val and val <= rightVal): # found location
                return mid_idx
            
            if (leftVal > val):
                high = mid_idx - 1
            elif (val > rightVal):
                low = mid_idx + 1
        
        return low
    
s = Solution()
la, lb = [1,2,3], [2,3,4]
print("median of {0} and {1} is {2}".format(la, lb, s.findMedianSortedArrays(la,lb)))
