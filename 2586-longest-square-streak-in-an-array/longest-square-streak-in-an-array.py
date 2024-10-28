class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        unique = set(nums)
        longest_streak = 0
        for i in unique:
            streak_length = 0
            while i in unique:
                streak_length += 1
                i *= i

            longest_streak = max(longest_streak , streak_length)

        return longest_streak if longest_streak >= 2 else -1