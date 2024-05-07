import math
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sqrt1 = math.sqrt(num)
        if sqrt1.is_integer():
            return True
        return False