# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy.next 
        
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next 
            else:
                curr = curr.next  
        
        return dummy.next
