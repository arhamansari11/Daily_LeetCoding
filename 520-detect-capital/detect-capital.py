class Solution:
    def detectCapitalUse(self, words: str) -> bool:
        if words.isupper():
            return True
        elif words.islower():
            return True
        elif words.istitle():
            return True
        else:
            return False