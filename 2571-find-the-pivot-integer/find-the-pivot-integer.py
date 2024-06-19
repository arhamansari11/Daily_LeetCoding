class Solution:
    def pivotInteger(self, n: int) -> int:
        arr = []
        i = 1
        while i <= n:
            arr.append(i)
            i += 1
        
        total_sum = sum(arr)
        leftsum = 0
        for i in range(len(arr)):
            if leftsum == (total_sum - leftsum - arr[i]):
                return arr[i]
            
            leftsum += arr[i]

        return -1
