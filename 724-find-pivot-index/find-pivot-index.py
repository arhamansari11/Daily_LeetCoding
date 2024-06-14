class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        leftsum = 0
        for i in range(len(nums)):
            if leftsum == (total_sum - leftsum - nums[i]):
                return i
            
            leftsum += nums[i]
        return -1