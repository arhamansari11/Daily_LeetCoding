class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        multiply = 0
        n = len(nums)
        for i in range(n):
            if n % (i+1) == 0:
                multiply += nums[i] * nums[i]

        return multiply

        
        