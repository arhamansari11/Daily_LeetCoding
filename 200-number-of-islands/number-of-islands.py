from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1 , 0] , [-1 , 0] , [0 , 1] , [0 , -1]] 
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0

        def bfs(r , c):
            q = deque()
            grid[r][c] = "0"
            q.append((r , c))
            while q:
                row , col = q.popleft()
                for dr , dc in directions:
                    nr = dr + row
                    nc = dc + col
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == "0"):
                        continue
                    q.append((nr , nc))
                    grid[nr][nc] = "0"

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r , c)
                    islands += 1

        return islands