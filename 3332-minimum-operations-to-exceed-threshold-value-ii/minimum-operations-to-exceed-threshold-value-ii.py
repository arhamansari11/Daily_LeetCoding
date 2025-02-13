class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        opt = 0
        while len(nums) > 1 and nums[0] < k:
            x = heappop(nums)
            y = heappop(nums)
            ans = (x * 2) + y
            heappush(nums , ans)
            opt += 1

        return opt