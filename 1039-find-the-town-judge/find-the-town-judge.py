class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        arr = [0] * (n + 1)
        
        for a , b in trust:
            arr[a] -= 1
            arr[b] += 1

        for i in range(1 , n + 1):
            if arr[i] == n - 1:
                return i

        return -1 