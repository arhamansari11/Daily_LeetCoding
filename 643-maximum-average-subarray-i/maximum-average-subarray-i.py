class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = windowSum = sum(nums[0:k])
        for i in range(len(nums)-k):
            windowSum = windowSum + nums[i+k] - nums[i]
            maxSum = max(maxSum , windowSum)
        return maxSum/k