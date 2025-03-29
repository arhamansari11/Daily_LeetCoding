class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # Length of N == 3
        # 2D array == 2
        edges1 = edges[0] # [1,2]
        edges2 = edges[1] # [2,3]
        if edges1[0] in edges2:
            return edges1[0]
        else:
            return edges1[1]