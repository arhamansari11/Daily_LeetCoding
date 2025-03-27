class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def helper(x):
            if x < 0:
                return 0            
            l = 0
            current = 0
            result = 0
            for r in range(len(nums)):
                current += nums[r]
                while current > x:
                    current -= nums[l]
                    l += 1
                result += (r - l + 1)
            return result

        return helper(goal) - helper(goal - 1)