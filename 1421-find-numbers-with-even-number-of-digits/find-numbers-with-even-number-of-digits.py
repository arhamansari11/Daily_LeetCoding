class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0

        for i in range(len(nums)):
            temp = 0
            while nums[i] > 0:
                nums[i] //= 10
                temp += 1

            if temp % 2 == 0:
                count += 1


        return count