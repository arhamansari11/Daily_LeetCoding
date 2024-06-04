class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        len1 = len(words)
        len2 = len(s)
        count = 0

        if len1 == len2:
            for i in range(len(words)):
                if words[i].startswith(s[i]):
                    count += 1

        if count == len1:
            return True
        else:
            return False

        