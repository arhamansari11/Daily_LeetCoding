class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge = nums1 + nums2
        merge.sort()

        length = len(merge)
        mid = length // 2

        if length % 2 == 0:
            mid = (merge[mid-1] + merge[mid]) / 2
        else:
            mid = merge[mid]

        return mid
