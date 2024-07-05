class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1 , -1]
        
        prev =  head
        curr = head.next
        critical = []
        index = 1

        while curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or (curr.val < prev.val and curr.val < curr.next.val ):
                critical.append(index)
            prev = curr
            curr = curr.next
            index += 1
        
        if len(critical) < 2:
            return [-1 , -1]
        
        minimum_check = float("inf")
        for i in range(1 , len(critical)):
            minimum_check = min(minimum_check , critical[i] - critical[i - 1])
        
        max_distance = critical[-1] - critical[0]
        return [minimum_check , max_distance]

