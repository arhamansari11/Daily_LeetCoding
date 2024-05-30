class Solution:
    def minimizedStringLength(self, s: str) -> int:
        # set1 = set(s)
        # string = ""
        # for i in set1:
        #     string += i

        # return len(string)

        string = ""

        for i in s:
            if i not in string:
                string += i

        return len(string)
