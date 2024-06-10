class Solution:
    def flipAndInvertImage(self, matrix: List[List[int]]) -> List[List[int]]:
        for i in range(len(matrix)):
            matrix[i].reverse()
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][j] = 1
                elif matrix[i][j] == 1:
                    matrix[i][j] = 0
        
        return matrix