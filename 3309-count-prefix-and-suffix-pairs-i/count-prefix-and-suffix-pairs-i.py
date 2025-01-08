class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            for j in range(len(words)):
                if i < j and words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    count += 1


        return count