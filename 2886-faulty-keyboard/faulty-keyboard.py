class Solution:
    def finalString(self, s: str) -> str:
        res = ""
        for i in s:
            if i != "i":
                res += i
            if i == "i":
                res = res[::-1]

        return res
