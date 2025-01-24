class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length = max( len(word1)  , len(word2))
        string = ""
        for i in range(length):
            if i < len(word1):
                string += word1[i]
            if i < len(word2):
                string += word2[i]


        return string
