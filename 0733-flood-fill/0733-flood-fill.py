class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        intial_color = image[sr][sc]
        global copy
        copy = []
        for i in range(len(image)):
            l = []
            for j in range(len(image[0])):
                l.append(image[i][j])
            copy.append(l)
        
        def dfs(image, copy, col, row, color, intial_color):
            rows = [-1,0,1,0]
            cols = [0,-1,0,1]
            copy[row][col] = color
            n = len(image)
            m = len(image[0])
            nrow = -1
            mcol = -1
            for i in range(4):
                nrow = row + rows[i]
                mcol = col + cols[i]
                if(nrow >= 0 and nrow < n and mcol >= 0 and mcol < m and image[nrow][mcol] == intial_color and copy[nrow][mcol]!= color):
                    copy = dfs(image,copy,mcol,nrow,color,intial_color)
            return copy
            
        copy2 = dfs(image, copy, sc, sr, color, intial_color)
        return copy2