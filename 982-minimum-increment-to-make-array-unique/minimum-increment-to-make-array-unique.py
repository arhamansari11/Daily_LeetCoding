class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        moves  = 0
        nums.sort()
        for i in range(1 , len(nums)):
            if nums[i-1] >= nums[i]:
                inc = nums[i-1] - nums[i] + 1
                nums[i] += inc
                moves += inc
        
        return moves