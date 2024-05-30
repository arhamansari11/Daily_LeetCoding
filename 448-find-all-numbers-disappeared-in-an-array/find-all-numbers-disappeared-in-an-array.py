class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set1 = set(nums)
        ans = []
        for i in range(1 , len(nums)+1):
            if i not in set1:
                ans.append(i)

        return ans
