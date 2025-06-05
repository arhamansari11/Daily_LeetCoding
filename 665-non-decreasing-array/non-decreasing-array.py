class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0  
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                count += 1
                if count > 1:
                    return False
                if i < 2 or nums[i] >= nums[i - 2]:
                    nums[i - 1] = nums[i]  
                else:
                    nums[i] = nums[i - 1]  
        return True
