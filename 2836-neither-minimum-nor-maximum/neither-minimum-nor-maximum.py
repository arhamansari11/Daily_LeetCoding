class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        minimum = min(nums)
        maximum = max(nums)

        for i in nums:
            if i != minimum and i != maximum:
                return i

        return -1