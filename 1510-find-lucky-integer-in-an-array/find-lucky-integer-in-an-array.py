class Solution:
    def findLucky(self, arr: List[int]) -> int:
        nums = [-1]
        set1 = set(arr)

        for i in set1:
            if arr.count(i) == i:
                nums.append(i)

        maximum = max(nums)

        return maximum