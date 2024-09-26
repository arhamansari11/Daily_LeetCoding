# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lesshead = ListNode(0)
        greathead = ListNode(0)
        less = lesshead
        great = greathead
        curr = head
        while curr:
            if curr.val < x:
                less.next = curr
                less = less.next
            else:
                great.next = curr
                great = great.next
            curr = curr.next
        great.next = None
        less.next = greathead.next
        return lesshead.next