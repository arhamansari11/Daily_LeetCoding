class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        subarrays = []
        for i in range(n):
            for j in range(i , n):
                sub = nums[i:j+1]
                subarrays.append(sum(sub))

        subarrays.sort()
        result = sum(subarrays[left-1:right]) % MOD
        
        return result