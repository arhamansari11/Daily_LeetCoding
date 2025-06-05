from typing import List

class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        non_increasing = [0] * n
        non_decreasing = [0] * n
        
        # Fill non-increasing prefix
        non_increasing[0] = 1
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                non_increasing[i] = non_increasing[i - 1] + 1
            else:
                non_increasing[i] = 1
        
        # Fill non-decreasing suffix
        non_decreasing[-1] = 1
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                non_decreasing[i] = non_decreasing[i + 1] + 1
            else:
                non_decreasing[i] = 1
        
        # Find all good indices
        result = []
        for i in range(k, n - k):
            if non_increasing[i - 1] >= k and non_decreasing[i + 1] >= k:
                result.append(i)
        
        return result
