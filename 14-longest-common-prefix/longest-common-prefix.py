class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        j = 1
        while j < len(strs):
            if strs[j].startswith(prefix):
                j += 1
            else:
                prefix = prefix[:-1]

        return prefix