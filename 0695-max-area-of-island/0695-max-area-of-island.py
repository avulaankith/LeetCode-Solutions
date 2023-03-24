class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # My Solution
        n = len(grid)
        m = len(grid[0])

        global visited
        visited = [[0 for j in range(m)] for i in range(n)]

        def dfs(grid ,i, j, visited):
            n = len(grid)
            m = len(grid[0])
            rows = [-1, 0, 1, 0]
            cols = [0, -1, 0, 1]
            visited[i][j] = 1
            
            for k in range(4):
                nrow = i + rows[k]
                mcol = j + cols[k]
                
                if (nrow >= 0 and nrow < n) and (mcol >= 0 and mcol < m) and (visited[nrow][mcol] == 0 and grid[nrow][mcol] == 1):
                    dfs(grid, nrow, mcol, visited)
        
        maxcount = 0
        count = 0
        old = []
        oldone = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dfs(grid,i,j,visited)
                    s = sum([sum(k) for k in visited])
                    old.append(s-oldone)
                    oldone = s
        maxi = 0
        for i in old:
            maxi = max(maxi, i)
        return maxi

        # Leetcode solution
        # class Solution:
        # def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #     n = len(grid)
        #     m = len(grid[0])

        #     visited = [[0 for j in range(m)] for i in range(n)]

        #     def dfs(i, j):
        #         if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 0: 
        #             return 0
        #         rows = [-1, 0, 1, 0]
        #         cols = [0, -1, 0, 1]
        #         grid[i][j] = 0
                
        #         return 1 + dfs(i-1,j) + dfs(i,j-1) + dfs(i+1,j) + dfs(i,j+1)
            
        #     maxcount = 0
        #     count = 0
        #     for i in range(n):
        #         for j in range(m):
        #             if grid[i][j] == 1:
        #                 count = dfs(i,j)
        #                 maxcount = max(maxcount,count)
            
        #     return maxcount
