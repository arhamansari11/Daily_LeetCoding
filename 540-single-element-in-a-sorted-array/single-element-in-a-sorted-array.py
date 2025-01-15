class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        count = Counter(nums)
        for i in nums:
            if count[i] == 1:
                return i