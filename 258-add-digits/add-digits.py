class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            digit = num % 10
            num = num // 10
            num += digit
        
        return num