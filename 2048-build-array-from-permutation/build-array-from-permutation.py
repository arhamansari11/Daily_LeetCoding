class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [0] * length
        for i in range(length):
            result[i] = nums[nums[i]]
        return result
        