class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Iterate through the nums array
        for num in nums:
            # Get the index corresponding to the absolute value of num - 1
            index = abs(num) - 1
            # If nums[index] is positive, mark it as visited by making it negative
            if nums[index] > 0:
                nums[index] *= -1
        # Iterate through the modified nums array to find which indices were not marked as visited
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                # If nums[i] is positive, it means that the number corresponding to index i + 1 did not appear in nums
                result.append(i + 1)
        return result
