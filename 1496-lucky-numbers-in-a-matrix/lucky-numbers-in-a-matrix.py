class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row = []
        col = []
        for i in range(len(matrix)):
            row.append(min(matrix[i]))

        for j in range(len(matrix[i])):
            maximum = max(matrix[i][j] for i in range(len(matrix)))
            col.append(maximum)
        
        common = list(set(row) & set(col))

        return common