class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s) // 2
        a = s[:n]
        b = s[n:]
        count1 = 0
        count2 = 0
        vowels = "aeiouAEIOU"
        for i in a:
            if i in vowels:
                count1 += 1
        for i in b:
            if i in vowels:
                count2 += 1

        if count1 == count2:
            return True

        return False