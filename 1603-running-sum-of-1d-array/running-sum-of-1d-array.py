class Solution:
    def runningSum(self, num: List[int]) -> List[int]:
        temp = 0
        arr = []
        for i in num:
            temp = temp + i
            arr.append(temp)

        return arr
        