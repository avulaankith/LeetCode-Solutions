class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        def dfs(adjl, visited, from_node):
            visited[from_node] = 1
            change = 0
            for i in adjl[from_node]:
                if visited[abs(i)] == 0:
                    change += dfs(adjl, visited, abs(i)) + (1 if i > 0 else 0)
            return change

        adjl = collections.defaultdict(dict)
        for u,v in connections:
            adjl[u][v] = 1
            adjl[v][-u] = 1
        visited = [0 for i in range(n)]
        return dfs(adjl,visited,0)

