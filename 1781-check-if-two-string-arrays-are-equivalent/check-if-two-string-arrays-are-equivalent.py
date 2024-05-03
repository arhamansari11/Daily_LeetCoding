class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        str1 = ""
        str2 = ""
        for i in range(len(word1)):
            str1 = str1 + word1[i]
        for i in range(len(word2)):
            str2 = str2 + word2[i]
        if str1 == str2:
            return True
        return False
        