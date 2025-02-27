# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        string = ""
        dummy = head
        while dummy:
            string += str(dummy.val)
            dummy = dummy.next
        
        integer = int(string  , 2)
        return integer