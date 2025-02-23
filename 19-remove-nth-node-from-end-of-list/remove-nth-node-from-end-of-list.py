# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        previous = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = previous
            previous = curr
            curr = nxt

        
        dummy = ListNode(0)
        dummy.next = previous
        current = dummy
        i = 0

        while current.next:
            i += 1
            if i == n:
                current.next = current.next.next
                break
            current = current.next


        previ = None
        curri = dummy.next
        while curri:
            nxt = curri.next
            curri.next = previ
            previ = curri
            curri = nxt

        return previ


        












        # How to find the Length of the Linked List

        # length = 0
        # curr = head
        # while curr:
        #     length  += 1
        #     curr = curr.next


        # print(length)