class Solution:
    def hammingWeight(self, n: int) -> int:
        # 1-> Binary Form
        # 2-> Count 1's

        bit = bin(n)
        split = bit[2:]
        counting = split.count('1')
        return counting