class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        mat2 = []
        for i in mat:
            l = []
            for j in i:
                l.append(j)
            mat2.append(l)

        q = collections.deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat2[i][j] == 0:
                    q.append((i,j))
                else:
                    mat2[i][j] = -1

        rows = [-1,0,1,0]
        cols = [0,-1,0,1]
        m = len(mat)
        n = len(mat[0])

        while(q):
            row,col = q.popleft()
            for i in range(4):
                mr = row + rows[i]
                nc = col + cols[i]

                if (mr < 0 or nc < 0 or mr >= m or nc >= n or mat2[mr][nc]!=-1):
                    continue
                mat2[mr][nc] = mat2[row][col] + 1
                q.append((mr,nc))
        
        return mat2
        
        