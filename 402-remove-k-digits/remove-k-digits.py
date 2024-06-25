class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        if len(nums) == k:
            return "0"
        stack = []

        for i in range(len(nums)):
            while stack and stack[-1] > nums[i] and k > 0:
                stack.pop()
                k -= 1
            stack.append(nums[i])
        
        stack = stack[:len(stack) - k]

        return "".join(stack).lstrip("0") or "0"