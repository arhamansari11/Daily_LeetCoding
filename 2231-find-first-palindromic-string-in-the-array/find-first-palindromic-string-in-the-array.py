class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        string = ""
        for i in words:
            if i == i[::-1]:
                string += i
                break

        return string