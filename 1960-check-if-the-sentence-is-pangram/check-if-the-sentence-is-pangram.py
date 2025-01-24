class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # string  = "abcdefghijklmnopqrstuvwxyz"

        # for i in string:
        #     if i in sentence:
        #         continue
        #     else:
        #         return False

        # return True

        set1 = set(sentence)
        if len(set1) == 26:
            return True

        return False