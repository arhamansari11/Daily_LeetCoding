class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        
        vowels = "aeiouAEIOU"
        has_vowel = False
        has_constant = False

        for char in word:
            if char.isalpha() or char.isdigit():
                if char in vowels:
                    has_vowel = True
                elif char.isalpha():
                    has_constant = True
            else:
                return False
        
        return has_vowel and has_constant