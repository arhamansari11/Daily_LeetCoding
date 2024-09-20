# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Brute Force Solution

        # arr = []
        # curr = head
        
        # while curr:
        #     arr.append(curr.val)
        #     curr = curr.next
        
        # arr.reverse()
        
        # current = head
        # for i in range(len(arr)):
        #     current.val = arr[i]
        #     current = current.next
        
        # return head

        #  Optimize Solution

        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

        