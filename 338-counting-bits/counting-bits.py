class Solution:
    def countBits(self, n: int) -> List[int]:
        i = 0
        arr = []
        while i <= n:
            bit = bin(i)
            split = bit[2:]
            counting = split.count('1')
            arr.append(counting)
            i += 1

        return arr

