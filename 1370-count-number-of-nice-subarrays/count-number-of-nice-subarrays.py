class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        count = 0
        prefix = 0
        res = 0
        odd = 0
        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                odd += 1
                prefix = 0
            while odd == k:
                if nums[left] % 2 == 1:
                    odd -= 1
                left += 1
                prefix += 1
            
            res += prefix
        
        return res
