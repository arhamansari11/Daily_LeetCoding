class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        maximum = max(nums)

        for i in range(len(nums)):
            if -maximum in nums:
                return maximum
            else:
                nums.remove(maximum)

                if not nums:
                    return -1

                maximum = max(nums)

        return maximum