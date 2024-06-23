class Solution:
    def finalPrices(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums)):
            found = False
            for j in range(i+1 , len(nums)):
                if nums[i] >= nums[j]:
                    arr.append(nums[i] - nums[j])
                    found = True
                    break
            if not found:
                arr.append(nums[i])

        return arr