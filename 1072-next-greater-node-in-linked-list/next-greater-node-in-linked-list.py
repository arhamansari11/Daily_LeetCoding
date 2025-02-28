# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        nums = []
        current = head
        while current:
            nums.append(current.val)
            current = current.next

        stack = []
        result = [0] * len(nums)
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                result[stack.pop()] = nums[i]
            stack.append(i)

        return result

        