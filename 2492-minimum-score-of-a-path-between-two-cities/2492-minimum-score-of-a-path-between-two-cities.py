from collections import deque, defaultdict
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        minimum = 99999999999999

        graph = defaultdict(dict)
        for u, v, w in roads:
            graph[u][v] = w
            graph[v][u] = w
        
        visited = set()

        queue = deque([1])

        while len(queue) > 0:
            val = queue.popleft()
            for v, w in graph[val].items():
                if v not in visited:
                    queue.append(v)
                    visited.add(v)
                minimum = min(minimum, w)
        
        return minimum
                