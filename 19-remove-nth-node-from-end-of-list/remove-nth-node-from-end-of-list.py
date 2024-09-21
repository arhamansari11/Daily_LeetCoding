class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        curr = head
        
        # Reverse the linked list
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # Remove the N-th node from the end
        dummy = ListNode(0)
        dummy.next = prev
        current = dummy
        i = 0
        
        while current.next:
            i += 1
            if i == n:
                current.next = current.next.next
                break
            current = current.next
        
        # Reverse the list back to original order
        previ = None
        curri = dummy.next
        while curri:
            nxt = curri.next
            curri.next = previ
            previ = curri
            curri = nxt
        
        return previ
