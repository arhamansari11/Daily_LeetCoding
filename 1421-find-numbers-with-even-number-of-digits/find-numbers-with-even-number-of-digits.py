class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            element = nums[i]
            digit = 0
            while element > 0:
                element = element // 10
                digit +=  1

            if digit % 2 == 0:
                count += 1
            
        return count