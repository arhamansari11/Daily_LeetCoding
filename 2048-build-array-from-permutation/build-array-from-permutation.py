class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums)):
            x = nums[i]
            desire_ans = nums[x]
            ans.append(desire_ans)

        return ans