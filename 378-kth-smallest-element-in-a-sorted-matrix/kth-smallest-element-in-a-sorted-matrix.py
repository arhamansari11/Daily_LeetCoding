class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = []
        for i in matrix:
            for j in i:
                arr.append(j)

        arr.sort()

        return arr[k-1]