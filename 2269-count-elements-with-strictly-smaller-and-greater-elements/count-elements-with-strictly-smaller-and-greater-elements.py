class Solution:
    def countElements(self, nums: List[int]) -> int:
        min_val = min(nums)
        max_val = max(nums)
        if min_val == max_val:
            return 0
        count = nums.count(min_val) + nums.count(max_val)
        n = len(nums)

        return n - count