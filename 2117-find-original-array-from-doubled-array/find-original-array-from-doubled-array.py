class Solution:
    def findOriginalArray(self, nums: List[int]) -> List[int]:
        if len(nums) % 2 != 0:
            return []
        
        nums.sort()
        freq =  Counter(nums)
        result = []
        for i in nums:
            if freq[i] == 0:
                continue
            if freq[i * 2] == 0:
                return []

            result.append(i)
            freq[i] -= 1
            freq[i * 2] -= 1
        
        return result