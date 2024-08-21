class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        matrix = []
        temp = []
        for i in mat:
            for j in i:
                temp.append(j)
        
        if len(temp) != r * c:
            return mat
        else:
            for i in range(r):
                matri = temp[i*c : (i*c) + c]
                matrix.append(matri)
        return matrix