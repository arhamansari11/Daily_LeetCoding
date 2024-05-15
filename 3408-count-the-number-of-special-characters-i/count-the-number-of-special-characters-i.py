class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower_set = set()
        upper_set = set()
    
        for char in word:
            if char.islower():
                lower_set.add(char)
            elif char.isupper():
                upper_set.add(char)
    
        # Find the intersection of the two sets
        special_letters = lower_set.intersection(char.lower() for char in upper_set)
        
        return len(special_letters)