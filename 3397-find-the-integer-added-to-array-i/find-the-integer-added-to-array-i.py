class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        x =  min(nums2) - min(nums1)
        return x