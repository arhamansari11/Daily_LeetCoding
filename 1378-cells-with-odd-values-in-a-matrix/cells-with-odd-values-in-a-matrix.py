class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        arr = [0] * (m * n)
        matrix = []
        for i in range(m):
            row = arr[i * n : (i + 1) * n  ]
            matrix.append(row)

        for row_idx , col_idx in indices:
            for col in range(n):
                matrix[row_idx][col] += 1
            for row in range(m):
                matrix[row][col_idx] += 1

        odd = 0
        for i in matrix:
            for j in i:
                if j % 2 != 0:
                    odd+= 1

        return odd