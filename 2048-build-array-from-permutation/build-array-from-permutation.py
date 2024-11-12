class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        for i in nums:
            ans[i] = nums[nums[i]]

        return ans