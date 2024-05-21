# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        current = head
        first = dummy
        while current:
            if current.val == val:
                first.next = current.next
            else:
                first = current
            current = current.next

        return dummy.next
