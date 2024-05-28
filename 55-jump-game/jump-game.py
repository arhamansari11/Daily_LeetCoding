class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jumps = 0
        for jumps in nums:
            if max_jumps < 0:
                return False
            max_jumps = max(max_jumps , jumps)
            max_jumps -= 1
        return True