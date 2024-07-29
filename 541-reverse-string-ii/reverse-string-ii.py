class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        string = ""
        i = 0
        while i < len(s):
            string += s[i : i+k][::-1]
            string += s[i+k : i + 2*k]
            i += 2 * k

        return string
