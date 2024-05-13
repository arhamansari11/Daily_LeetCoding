class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        set1 = set(nums)

        count = {num : nums.count(num) for num in set1}

        return max(count , key = count.get)
        
