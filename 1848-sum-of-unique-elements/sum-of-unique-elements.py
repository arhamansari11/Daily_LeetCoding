class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        unique = 0
        for i in nums:
            if nums.count(i) == 1:
                unique += i

        return unique