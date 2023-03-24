class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        visited = [[0 for j in range(m)] for i in range(n)]

        def dfs(i, j):
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 0: 
                return 0
            rows = [-1, 0, 1, 0]
            cols = [0, -1, 0, 1]
            grid[i][j] = 0
            
            return 1 + dfs(i-1,j) + dfs(i,j-1) + dfs(i+1,j) + dfs(i,j+1)
        
        maxcount = 0
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count = dfs(i,j)
                    maxcount = max(maxcount,count)
        
        return maxcount
