class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        temp = 0
        arr = []
        for i in nums:
            temp = temp + i
            arr.append(temp)

        return arr