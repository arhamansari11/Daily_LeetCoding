from typing import List 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Brute force with TC -> O(n^2)
        """for i in range(len(nums)-1):
            for j in range(i+1 , len(nums)):
                if nums[i] + nums[j] == target:
                    ans = [i, j]
                    return ans"""
        
        # Optimal solution with TC -> O(n)
        hash_map = {}
        for ind, value in enumerate(nums):
            diff = target - value
            if diff in hash_map:
                return [hash_map[diff], ind]
            hash_map[value] = ind
        return 