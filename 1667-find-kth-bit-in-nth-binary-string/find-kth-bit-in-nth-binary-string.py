class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Base case: S1 is "0"
        if n == 1:
            return '0'

        # Calculate the middle position of Sn
        mid = 2 ** (n - 1)

        # If k is the middle bit, return '1'
        if k == mid:
            return '1'

        # If k is less than the middle, search in Sn-1
        elif k < mid:
            return self.findKthBit(n - 1, k)

        # If k is greater than the middle, invert the result from Sn-1
        else:
            return '0' if self.findKthBit(n - 1, mid - (k - mid)) == '1' else '1'
