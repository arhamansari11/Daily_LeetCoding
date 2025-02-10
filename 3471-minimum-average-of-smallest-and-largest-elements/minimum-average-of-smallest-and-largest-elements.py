class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        l = 0
        r = len(nums) - 1
        average = []
        while l  <=  r:
            addition = (nums[l] + nums[r] ) / 2
            average.append(addition)
            l += 1
            r -= 1

        return min(average)

