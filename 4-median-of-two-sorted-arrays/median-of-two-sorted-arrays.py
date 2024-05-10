from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        for i in range(len(nums2)):
            nums1.append(nums2[i])

        nums1.sort()

        length = len(nums1)
        mid = length // 2

        if length % 2 == 0:  # If length is even
            mid = (nums1[mid-1] + nums1[mid]) / 2
        else:
            mid = nums1[mid]
        
        return mid
