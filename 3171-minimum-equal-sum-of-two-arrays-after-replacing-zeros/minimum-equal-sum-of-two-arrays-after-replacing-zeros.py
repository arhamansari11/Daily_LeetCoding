class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zero1 = nums1.count(0)
        zero2 = nums2.count(0)

        sum1 = sum(nums1)+zero1
        sum2 = sum(nums2)+zero2

        if sum1<sum2 and zero1==0 or sum2<sum1 and zero2==0:
            return -1

        res = max(sum1,sum2)
        return res
        

            