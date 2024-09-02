class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        add = sum(chalk)
        k %= add

        for i in range(len(chalk)):
            if chalk[i] > k:
                return i
            k -= chalk[i]