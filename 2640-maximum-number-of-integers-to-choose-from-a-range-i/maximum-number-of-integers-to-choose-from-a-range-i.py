class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)
        current_sum = 0
        count = 0
        for i in range(1 , n + 1):
            if i not in banned_set and current_sum + i <= maxSum:
                current_sum += i
                count += 1

        return count