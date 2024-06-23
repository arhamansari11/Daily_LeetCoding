class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)  # size of the array.
         #[2,1,5,4,3,0,0]
        # Step 1: Find the break point:
        ind = -1  # break point
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                # index i is the break point
                ind = i
                break
       #[5,4,3,2,1]
        # If break point does not exist:
        if ind == -1:
            # reverse the whole array:
            nums.reverse()
            return

        # Step 2: Find the next greater element
        #         and swap it with nums[ind]:
        for i in range(n - 1, ind, -1):
            if nums[i] > nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i]
                break

        # Step 3: reverse the right half:
        nums[ind + 1:] = reversed(nums[ind + 1:])