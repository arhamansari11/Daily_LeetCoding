class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        arr = []

        for _ in range (len(nums) // 2):
            a = max(nums)
            b = min(nums)
            avg = (a+b) / 2
            arr.append(avg)
            nums.remove(a)
            nums.remove(b)
        
        return len(set(arr))