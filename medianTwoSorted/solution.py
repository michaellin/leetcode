from typing import *

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # case odd num of elements
        # case even num of elements
        m_odd = len(nums1) % 2
        n_odd = len(nums2) % 2
        m_n_odd = (len(nums1) + len(nums2)) % 2
        
        med_1_idx = len(nums1)//2
        med_nums1 = nums1[med_1_idx]
        # binary search on nums2
        insert_idx = self.binarySearchInsertIdx(med_nums1, nums2)
        
        # how many elements to the right and to the left
        right_elems = len(nums2) - insert_idx
        left_elems = insert_idx
        
        med_res = med_nums1
        # if all nums odd then search until left and right are equal
        if (m_n_odd):
            while (right_elems != left_elems):
            med_res = 
        # if all nums even then search until left larger than right by 1
        else:
            
        ###
        
        if (m_odd and n_odd or m_odd):    # both odd
            med_nums1 = nums1[len(nums1)//2]
            # binary search on nums2
            insert_idx = self.binarySearchInsertIdx(med_nums1, nums2)
            
        elif (n_odd):           # nums2 odd
            med_nums2 = nums2[len(nums2)//2]
            # binary search on nums2
            insert_idx = self.binarySearchInsertIdx(med_nums2, nums1)
        else:                    # both even
            continue
            
        # how many elements to the right and to the left
        right_elems = len(nums2)-insert_idx
        left_elems = insert_idx
        
        shift = right_elems - left_elems
        while (shift != 0):
            
        # find the median of nums1 first
        
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
    
    # 0, [1,2,3,6,7,8]
    # low = 0   high = 0
    # mid_idx = 0
        
    # leftVal = 1, rightVal = 2
    
    # 0, [3]
    # low = 0   high = 1
    # mid_idx = 1
        
    # leftVal = 1, rightVal = 2
