class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        edges_cnt = [0] * n
        for n1 , n2 in roads:
            edges_cnt[n1] += 1
            edges_cnt[n2] += 1
        label = 1
        res = 0
        for count in sorted(edges_cnt):
            res += label * count
            label += 1
    
        return res