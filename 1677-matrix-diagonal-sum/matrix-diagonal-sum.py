class Solution:
    def diagonalSum(self, matrix: List[List[int]]) -> int:
        add = 0
        r = len(matrix[0])-1
        for i in range(len(matrix)):
            add += matrix[i][i]
            add += matrix[i][r]
            r -= 1
        
        if len(matrix) % 2 != 0:
            add -= matrix[len(matrix) // 2][len(matrix) // 2]
        

        return add
