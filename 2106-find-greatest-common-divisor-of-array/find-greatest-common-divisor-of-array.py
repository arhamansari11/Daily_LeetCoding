import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        answer = math.gcd(min(nums) , max(nums))
        return answer
        