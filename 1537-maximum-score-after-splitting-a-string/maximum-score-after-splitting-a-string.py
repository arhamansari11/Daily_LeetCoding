class Solution:
    def maxScore(self, s: str) -> int:
        total_ones = s.count('1')
        left = 0
        right = total_ones
        max_count  = 0
        for i in range(len(s) - 1):
            if s[i] == "0":
                left += 1
            else:
                right -= 1

            max_count = max(max_count , left + right)

        return max_count
        