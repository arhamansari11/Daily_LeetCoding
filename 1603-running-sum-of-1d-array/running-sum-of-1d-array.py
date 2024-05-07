class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum1 = 0
        array = [] 
        for i in range(len(nums)):
            sum1 = sum1 + nums[i]
            array.append(sum1)
        return array