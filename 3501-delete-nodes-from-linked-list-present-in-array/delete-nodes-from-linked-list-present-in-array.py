# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        # Use a set for nums to enable O(1) lookup times
        nums_set = set(nums)  # No duplicates, so set is optimal
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        
        # Traverse and modify the linked list
        while curr.next:
            if curr.next.val in nums_set:  # Efficient O(1) lookup
                curr.next = curr.next.next  # Remove the node by skipping it
            else:
                curr = curr.next  
                
        return dummy.next
