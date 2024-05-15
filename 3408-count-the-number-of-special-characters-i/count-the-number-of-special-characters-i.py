class Solution:
    def numberOfSpecialChars(self, word: str) -> int:

        word = set(word)
        count = 0

        for i in word:
            if i.lower() == i:
                if i.upper() in word:
                    count += 1
        
        return count