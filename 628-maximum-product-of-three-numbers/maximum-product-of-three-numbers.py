from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Sort the list
        nums.sort()
        
        # The maximum product of three numbers can be:
        # 1. The product of the three largest numbers
        # 2. The product of the two smallest numbers and the largest number
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
