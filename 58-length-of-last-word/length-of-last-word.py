class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.strip()
        words = s.split()
        length = len(words)
        string = words[length-1]
        return len(string)
