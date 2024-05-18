class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        boolean = False

        for i in range(len(nums)):
            if nums[i] == target:
                boolean = True
        
        return boolean