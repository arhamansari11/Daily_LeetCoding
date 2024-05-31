class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        maximum = max(nums)

        while True:
            if -maximum in nums:
                break
            else:
                nums.remove(maximum)

                if not nums:
                    return -1

                maximum = max(nums)

        return maximum
