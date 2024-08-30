class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        # Brute Force Solution 

        # consistent = 0
        # for i in range(len(words)):
        #     count = 0
        #     for j in range(len(words[i])):
        #         if words[i][j] in allowed:
        #             count += 1

        #     if count == len(words[i]):
        #         consistent += 1

        # return consistent

        l =  list(allowed)
        c = 0
        for i in words:
            if set(i).issubset(l):
                c += 1
        return c