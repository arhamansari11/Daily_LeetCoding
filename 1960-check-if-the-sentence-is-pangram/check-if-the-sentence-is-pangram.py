class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        x = set(sentence)

        if len(x) == 26:
            return True
        
        return False