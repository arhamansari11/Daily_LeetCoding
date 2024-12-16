class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while k != 0:
            minimum = min(nums)
            index = nums.index(minimum)
            nums[index] = minimum * multiplier
            k -= 1

        return nums