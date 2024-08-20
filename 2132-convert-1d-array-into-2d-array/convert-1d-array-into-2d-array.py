class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != (m * n):
            return []
        
        arr = [] 

        for i in range(m):
            two = original[i * n : (i+1) * n]
            arr.append(two)

        return arr