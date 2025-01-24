class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        string  = "abcdefghijklmnopqrstuvwxyz"

        for i in string:
            if i in sentence:
                continue
            else:
                return False

        return True