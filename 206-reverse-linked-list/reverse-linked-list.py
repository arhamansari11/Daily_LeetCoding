# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr = head
        
        # Collect values from the linked list into an array
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        # Reverse the array with node values
        arr.reverse()
        
        # Rebuild the linked list using the reversed values
        current = head
        for i in range(len(arr)):
            current.val = arr[i]
            current = current.next
        
        return head
