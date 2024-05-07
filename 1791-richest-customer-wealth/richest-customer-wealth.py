class Solution:
    def maximumWealth(self, nums: List[List[int]]) -> int:
        newarr = []
        for i in range(len(nums)):
            plus = sum(nums[i])
            newarr.append(plus)
        maximum = max(newarr)
        return maximum