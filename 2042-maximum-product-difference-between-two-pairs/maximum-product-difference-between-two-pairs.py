class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        p1 = nums[0] * nums[1]
        p2 = nums[-1] * nums[-2]

        return p2 - p1