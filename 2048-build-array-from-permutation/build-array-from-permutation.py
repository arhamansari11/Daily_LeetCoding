class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        for i in range(len(nums)):
            element = nums[i]
            index = nums[element]
            ans[i] = index

        return ans