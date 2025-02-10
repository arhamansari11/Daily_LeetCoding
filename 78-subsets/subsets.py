class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            new_subset = [subset + [num] for subset in result]
            result += new_subset
        
        return result