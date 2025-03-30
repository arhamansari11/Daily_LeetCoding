class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
            row = len(grid)
            cols = len(grid[0])
            visited = set()
            def dfs(i , j):
                if i < 0 or j < 0 or i >= row or j >= cols or grid[i][j] == 0:
                    return 1
                if (i , j) in visited:
                    return 0
                visited.add((i , j))
                perim = dfs(i , j + 1)
                perim += dfs(i + 1 , j)
                perim += dfs(i , j - 1)
                perim += dfs(i -  1, j)
                return perim


            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j]:
                        return dfs(i , j)
