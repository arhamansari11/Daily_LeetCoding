class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        unique = [num for num in nums if nums.count(num) == 1]

        minimum = min(unique)

        return minimum