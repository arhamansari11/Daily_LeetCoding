class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        arr = []
        for i in grid:
            for j in i:
                arr.append(j)
        res = []
        for i in arr:
            if arr.count(i) == 2:
                res.append(i)
                break
        
        seen = set(arr)
        for i in range(1 , len(arr)+1):
            if i not in seen:
                res.append(i)
                break
        
        return res


            