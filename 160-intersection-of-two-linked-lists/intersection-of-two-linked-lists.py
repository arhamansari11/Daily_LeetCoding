class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA == None or headB == None:
            return None
        
        nodeA = headA
        nodeB = headB
        while nodeA != nodeB:
            if nodeA == None:
                nodeA = headB
            else:
                nodeA = nodeA.next
            if nodeB == None:
                nodeB = headA
            else:
                nodeB = nodeB.next
        return nodeB