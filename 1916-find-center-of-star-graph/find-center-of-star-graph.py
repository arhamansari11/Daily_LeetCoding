class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edges1 = edges[0]
        edges2 = edges[1]

        if edges1[0] in edges2:
            return edges1[0]
        else:
            return edges1[1]