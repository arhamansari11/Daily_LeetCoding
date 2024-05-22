class Solution:
    def numberOfSpecialChars(self, word: str) -> int:

        set1 = set(word)
        count = 0
        for i in set1:
            if i.lower() == i:
                if i.upper() in set1:
                    count += 1

        return count

