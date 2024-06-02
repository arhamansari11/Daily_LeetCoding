class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        set1 = set(nums)
        length = len(nums) + 1

        for i in range(length):
            if i not in set1:
                return i