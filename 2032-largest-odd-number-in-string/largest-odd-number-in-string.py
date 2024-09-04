class Solution:
    def largestOddNumber(self, num: str) -> str:
        if int(num[-1]) % 2 != 0:
            return num
        
        # Iterate from the end of the string to find the last odd digit
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 != 0:
                return num[:i + 1]
        
        # If no odd digit is found, return an empty string
        return ""
