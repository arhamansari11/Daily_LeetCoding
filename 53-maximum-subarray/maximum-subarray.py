class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        current_sum = 0
        for num in nums:
            current_sum += num
            max_sum = max(current_sum , max_sum)
            if current_sum < 0:
                current_sum = 0

        return max_sum