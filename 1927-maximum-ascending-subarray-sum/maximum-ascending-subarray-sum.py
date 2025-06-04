class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maximum = []
        current = nums[0]
        for i in range(1 , len(nums)):
            if nums[i] > nums[i-1]:
                current += nums[i]
            else:
                maximum.append(current)
                current = nums[i]
        maximum.append(current)
        return max(maximum)