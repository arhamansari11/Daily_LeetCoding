class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # Brute Force Solution

        # unique = set(nums)
        # if len(unique) != len(nums):
        #     return True
        # return False

        # Other Approach

        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False