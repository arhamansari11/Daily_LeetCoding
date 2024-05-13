class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        
        count = 0
        for i in range(len(patterns)):
            if patterns[i] in word:
                count += 1
        
        return count