class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dic and dic[complement] != i:
                return [i, dic[complement]]
