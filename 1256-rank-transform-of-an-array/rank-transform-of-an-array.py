class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s = set(arr)
        l = list(sorted(s))
        d = {}
        for i , j in enumerate(l):
            d[j] = i+1
        
        for i in range(len(arr)):
            arr[i] = d[arr[i]]

        return arr