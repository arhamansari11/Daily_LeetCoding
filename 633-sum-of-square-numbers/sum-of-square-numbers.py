class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(c ** 0.5)
        
        while left <= right:
            multiply = left * left + right * right
            if multiply == c:
                return True
            elif multiply > c:
                right -= 1
            else:
                left += 1
                
        return False
