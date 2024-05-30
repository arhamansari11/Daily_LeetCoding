class Solution:
    def minimizedStringLength(self, s: str) -> int:
        set1 = set(s)
        string = ""
        for i in set1:
            string += i

        return len(string)