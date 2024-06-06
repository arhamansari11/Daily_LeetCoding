class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        arr = []
        for i in range(len(nums)):
            if nums[i] == target:
                arr.append(i)
        if not arr:
            return [-1 , -1]
        return [arr[0] , arr[-1]]
