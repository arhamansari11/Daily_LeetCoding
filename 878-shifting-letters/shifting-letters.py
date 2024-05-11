class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        ans = ""
        sum1 =  sum(shifts)

        string = "abcdefghijklmnopqrstuvwxyz"

        for i in range(len(s)):
            ans += string[((ord(s[i]) - ord('a')) + sum1) % 26]
            sum1 -= shifts[i]

        return ans
