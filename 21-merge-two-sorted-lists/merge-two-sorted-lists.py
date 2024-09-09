class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        Current = dummy
        while l1 and l2:
            if l1.val < l2.val:
                Current.next = l1
                l1 = l1.next
            else:
                Current.next = l2
                l2 = l2.next
            Current = Current.next
        Current.next = l1 or l2
        return dummy.next