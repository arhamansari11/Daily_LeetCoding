class Solution:
    def arraySign(self, nums: List[int]) -> int:
        mult = 1
        for i in nums:
            mult = mult * i

        if mult >= 1:
            return 1
        elif mult < 0:
            return -1
        else:
            return 0