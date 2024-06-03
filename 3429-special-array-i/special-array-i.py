class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1):
            current = nums[i]
            next_element = nums[i+1]
            if current % 2 == next_element % 2:
                return False
        
        return True
