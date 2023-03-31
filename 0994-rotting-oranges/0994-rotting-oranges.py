class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = []
        queue = collections.deque()
        freshCount = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(len(grid)):
            l = []
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append([i,j,0])
                    l.append(grid[i][j])
                    continue
                elif grid[i][j] == 1:
                    freshCount += 1
                l.append(0)
                
            visited.append(l)
        time = 0
        cnt = 0
        while len(queue) > 0:
            ele = queue.popleft()
            i = ele[0]
            j = ele[1]
            t = ele[2]
            time = max(time,t)

            rows = [-1,0,1,0]
            cols = [0,-1,0,1]

            for k in range(4):
                row = i + rows[k]
                col = j + cols[k]
                if (row >= 0 and row < n and col >= 0 and col < m and grid[row][col]==1 and visited[row][col] == 0):
                    queue.append([row,col,t+1])
                    visited[row][col] = 2
                    cnt += 1
        if cnt != freshCount:
            return -1
        else:
            return time
            

