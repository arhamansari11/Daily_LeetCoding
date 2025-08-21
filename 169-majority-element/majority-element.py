class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}

        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        max_key = None
        max_value = -1

        for k in dic:
            if dic[k] > max_value:
                max_key = k
                max_value = dic[k]

        return max_key
