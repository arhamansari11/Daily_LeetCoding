class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # arr = []
        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(len(nums)):
        #         if i != j:
        #             if nums[i] > nums[j] :
        #                 count += 1

        #     arr.append(count)

        # return arr

        # a = set(nums)
        # {1 ,2 , 3 , 8}
        # arr = list(nums)
        #  [1 ,2 ,3 ,8]
        num = sorted(nums)
        dictionary = {}
        for i in range(len(num)):
            if num[i] not in dictionary:
                dictionary[num[i]] = i
        ans = []
        for j in range(len(nums)):
            ans.append(dictionary[nums[j]])

        return ans
