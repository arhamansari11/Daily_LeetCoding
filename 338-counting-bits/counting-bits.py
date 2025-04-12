class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        for i in range(n + 1):
            bit = bin(i)
            split = bit[2:]
            counting = split.count('1')
            arr.append(counting)

        return arr