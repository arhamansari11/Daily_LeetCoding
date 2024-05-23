class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.split()
        string = ""
        for i in x:
            string += i[::-1] + " "

        return string.rstrip()