class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        i = 1
        while i in set_nums:
            i += 1
        
        return i