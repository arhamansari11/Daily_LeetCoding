from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        val1 = 0
        # Count pairs where nums[left] + nums[right] <= upper
        while left < right:
            if nums[left] + nums[right] <= upper:
                val1 += right - left
                left += 1
            else:
                right -= 1  # Decrement right instead of increment

        val2 = 0
        left = 0
        right = len(nums) - 1
        # Count pairs where nums[left] + nums[right] < lower
        while left < right:
            if nums[left] + nums[right] < lower:
                val2 += right - left
                left += 1
            else:
                right -= 1

        return val1 - val2
