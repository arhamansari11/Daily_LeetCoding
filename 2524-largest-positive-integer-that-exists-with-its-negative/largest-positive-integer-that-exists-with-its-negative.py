class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            maximum = max(nums)
            if -maximum in nums:
                return maximum
            else:
                nums.remove(maximum)
                if not nums:
                    return -1

                maximum = max(nums)

        
           