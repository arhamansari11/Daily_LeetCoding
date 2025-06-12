class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        maximum = abs(nums[0] - nums[-1])

        for i in range(len(nums)-1):
            add =  abs(nums[i] - nums[i+1])
            if add > maximum:
                maximum = add

        return maximum