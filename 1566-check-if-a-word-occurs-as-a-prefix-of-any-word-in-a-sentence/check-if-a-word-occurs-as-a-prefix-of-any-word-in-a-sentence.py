class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        a = sentence.split()
        for i in range(len(a)):
            if a[i].startswith(searchWord):
                return i + 1

        return -1