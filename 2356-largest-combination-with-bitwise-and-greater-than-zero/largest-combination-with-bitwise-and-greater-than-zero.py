class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        max_count = 0
        for bit in range(32):
            count = 0
            for num in candidates:
                if num & (1 << bit):
                    count += 1

            max_count =  max(count , max_count)

        return max_count
