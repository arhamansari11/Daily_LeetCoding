class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        vowels = {"a" , "e" , "i" , "o" , "u"}
        total_sum = 0

        for i , ch in enumerate(word):
            if ch in vowels:
                total_sum += (i+1) * (n-i)

        return total_sum
