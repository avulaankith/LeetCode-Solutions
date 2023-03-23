from collections import defaultdict

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(dict)
        edgecount = 0
        for u, v in connections:
            edgecount += 1
            adj[u][v] = 1
            adj[v][u] = 1
        
        visited = set()
        def dfs(visited, adjl, node):
            visited.add(node)
            for i in adjl[node]:
                if i not in visited:
                    dfs(visited, adjl, i)
        count = 0

        for i in range(n):
            if i not in visited:
                count += 1
                dfs(visited,adj,i)
        if len(connections) < n - 1:
            return -1
        
        return count-1