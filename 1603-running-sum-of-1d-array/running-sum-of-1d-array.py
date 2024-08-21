class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            ans.append(count)

        return ans