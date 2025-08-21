class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums.sort()

        i = 0
        j = 1

        while j < len(nums):
            if nums[i] > nums[j]:
                nums[i] , nums[j] = nums[j] , nums[i]
                i = 0
                j = 1
            else:
                i += 1
                j += 1
            