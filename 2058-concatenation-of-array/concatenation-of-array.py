class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums.copy()

        for i in nums:
            ans.append(i)

        return ans