class Solution:
	def floodFill(self, image, sr, sc, newColor):
		#Code here
		copy = []
		for i in range(len(image)):
		    l = []
		    for j in range(len(image[0])):
		        l.append(image[i][j])
		    copy.append(l)
		initial_color = image[sr][sc]
		
		def dfs(copy, image, color, initial_color, row, col):
		    rows = [-1,0,1,0]
		    cols = [0,-1,0,1]
		    n = len(image)
		    m = len(image[0])
		    
		    copy[row][col] = color
		    nrow = -1
		    mcol = -1
		    for i in range(4):
		        nrow = row + rows[i]
		        mcol = col + cols[i]
		        
		        if (nrow >= 0 and nrow < n and mcol >= 0 and mcol < m and image[nrow][mcol] == initial_color and copy[nrow][mcol] != color):
		            copy = dfs(copy, image, color, initial_color, nrow, mcol)
		    return copy
		 
    	result = dfs(copy,image, newColor, initial_color, sr, sc)
    	return result



#{ 
 # Driver Code Starts
import sys
sys.setrecursionlimit(10**7)
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n)
		m = int(m)
		image = []
		for _ in range(n):
			image.append(list(map(int, input().split())))
		sr, sc, newColor = input().split()
		sr = int(sr); sc = int(sc); newColor = int(newColor);
		obj = Solution()
		ans = obj.floodFill(image, sr, sc, newColor)
		for _ in ans:
			for __ in _:
				print(__, end = " ")
			print()
# } Driver Code Ends