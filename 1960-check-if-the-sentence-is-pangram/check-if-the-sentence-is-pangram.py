class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        string1 = sentence
        x = set(string1)
        sortedx = sorted(x)
        length = len(sortedx)
        if length == 26:
            return True
        return False
        
