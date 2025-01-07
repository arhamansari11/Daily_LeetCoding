class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        arr = []
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i] != words[j] and words[i] in words[j]:
                    if words[i] not in arr:
                        arr.append(words[i])


        return arr