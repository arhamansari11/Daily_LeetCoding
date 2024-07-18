class Solution:
    def reverseString(self, nums: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            nums[left] , nums[right] = nums[right] , nums[left]
            left += 1
            right -= 1
            