class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        half = n // 2
        first = s[:half]
        second = s[half:]
        count1 = 0
        count2 = 0
        vowels = "aeiouAEIOU"
        for i in first:
            if i in vowels:
                count1 += 1
        for i in second:
            if i in vowels:
                count2 += 1
        
        return count1 == count2