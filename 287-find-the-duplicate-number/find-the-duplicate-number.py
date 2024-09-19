class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for i in nums:
            if i in seen:
                return i
            else:
                seen.add(i)