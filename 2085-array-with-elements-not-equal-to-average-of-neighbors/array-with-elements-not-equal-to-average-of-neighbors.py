class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        mid = len(nums) // 2

        left , right = nums[:mid] , nums[mid:]
        result = []
        i , j = 0  , 0

        while i < len(left) or j < len(right):
            if j < len(right):
                result.append(right[j])
                j += 1
            if i < len(left):
                result.append(left[i])
                i += 1

        return result
