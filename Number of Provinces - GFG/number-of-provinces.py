#User function Template for python3
from collections import defaultdict
class Solution:
    def numProvinces(self, adj, V):
        # code here 
        adjl = defaultdict(dict)
        for i in range(V):
            for j in range(V):
                if adj[i][j] == 1 and i!=j:
                    adjl[i][j] = adj[i][j]
                    adjl[j][i] = adj[i][j]
        
        visited = set()
        def dfs(visited, adjl, node):
            visited.add(node)
            for i in adjl[node]:
                if i not in visited:
                    dfs(visited, adjl, i)
        count = 0
        for i in range(V):
            if i not in visited:
                count += 1
                dfs(visited, adjl, i)
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        V=int(input())
        adj=[]
        
        for i in range(V):
            temp = list(map(int,input().split()))
            adj.append(temp);
        
        ob = Solution()
        print(ob.numProvinces(adj,V))
# } Driver Code Ends