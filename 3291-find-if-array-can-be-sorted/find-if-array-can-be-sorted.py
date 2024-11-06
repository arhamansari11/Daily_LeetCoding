class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        if nums == sorted(nums):
            return True
        d = {}
        for i in nums:
            d[i] = bin(i).count("1")
        t = sorted(nums)
        while True:
            for i in range(len(nums) - 1):
                if nums[i] > nums[i+1] and d[nums[i]] != d[nums[i+1]]:
                    return False
                elif nums[i] > nums[i+1] and d[nums[i]] == d[nums[i+1]]:
                    nums[i] , nums[i+1] = nums[i+1] , nums[i]

            if t == nums:
                return True

