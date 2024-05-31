class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        addition = 0
        arr = []

        for i in range(len(nums)):
            addition = addition + nums[i]
            arr.append(addition)

        return arr
