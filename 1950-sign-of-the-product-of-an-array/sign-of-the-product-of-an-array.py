import math
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = math.prod(nums)

        if ans > 0:
            return 1
        elif ans < 0:
            return -1
        else:
            return 0

