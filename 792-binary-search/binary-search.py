class Solution:
    def search(self, nums: List[int], target: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1