class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[0 for j in range(m)] for i in range(n)]
        count = 0
        for i in range(n):
            for j in range(m):
                if visited[i][j] == 0 and grid[i][j] == "1":
                    count += 1
                    self.dfs(grid, i, j, visited)
        return count

    def dfs(self, grid ,i, j, visited):
        n = len(grid)
        m = len(grid[0])
        rows = [-1, 0, 1, 0]
        cols = [0, -1, 0, 1]
        visited[i][j] = 1
        
        for k in range(4):
            nrow = i + rows[k]
            mcol = j + cols[k]
            
            if (nrow >= 0 and nrow < n) and (mcol >= 0 and mcol < m) and (visited[nrow][mcol] == 0 and grid[nrow][mcol] == "1"):
                self.dfs(grid, nrow, mcol, visited)