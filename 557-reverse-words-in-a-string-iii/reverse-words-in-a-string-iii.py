class Solution:
    def reverseWords(self, s: str) -> str:
        str1 = ""
        x = s.split()
        for i in range(len(x)):
            str1 = str1 + x[i][::-1] + " "

        return str1.rstrip()