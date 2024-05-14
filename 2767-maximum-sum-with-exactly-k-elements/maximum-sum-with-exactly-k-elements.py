class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:

        sums = max(nums)

        for i in range(sums+1 , sums+k):
            sums += i

        return sums

        