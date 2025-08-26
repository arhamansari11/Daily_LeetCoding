class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums) // 3

        dic = {}

        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        arr = []

        for i , j in dic.items():
            if j > n:
                arr.append(i)
                
        return arr