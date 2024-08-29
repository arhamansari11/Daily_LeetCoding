class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        hashm = []
        for i in range(len(mat)):
            hashm.append([mat[i].count(1) , i])
        hashm.sort()
        res = []
        for i in range(k):
            res.append(hashm[i][1])

        return res