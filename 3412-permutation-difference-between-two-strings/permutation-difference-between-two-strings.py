class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        addition = 0
        for i in range(len(s)):
            index = t.find(s[i])
            addition += abs(i - index)

        return addition