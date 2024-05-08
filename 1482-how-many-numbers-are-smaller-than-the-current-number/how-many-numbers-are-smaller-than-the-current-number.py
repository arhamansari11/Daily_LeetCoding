class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        array = [0] * len(nums)

        for i in range(len(nums)):
            count = 0
            maxval = nums[i]

            for j in range(len(nums)):

                if maxval > nums[j]:

                    count += 1
                    array[i] = count

        return array