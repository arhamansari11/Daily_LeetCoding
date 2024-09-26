class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        curr = head
        
        # Convert linked list to array
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        l = 0
        r = len(arr) - 1
        maximum = 0  # Initialize maximum to track the highest pair sum
        
        # Calculate the pair sums
        while l < r:  # Change condition to l < r
            maximum = max(maximum, arr[l] + arr[r])  # Keep track of the maximum sum
            l += 1
            r -= 1
        
        return maximum
