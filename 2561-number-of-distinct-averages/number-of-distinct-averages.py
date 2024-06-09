class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        arr = []
        while len(nums) >= 2:
           a = min(nums)
           b = max(nums)
           average = (a + b)/2
           arr.append(average)
           nums.remove(a)
           nums.remove(b)

        return len(set(arr))