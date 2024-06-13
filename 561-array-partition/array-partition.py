class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        arr = []
        length = len(nums)//2
        for i in range(len(nums) - length):
            minimum = min(nums[2 * i] , nums[2*i +1])
            arr.append(minimum)
        return sum(arr)