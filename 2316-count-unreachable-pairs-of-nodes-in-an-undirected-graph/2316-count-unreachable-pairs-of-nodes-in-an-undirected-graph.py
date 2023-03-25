from collections import defaultdict
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        adjl = defaultdict(dict)
        for u, v in edges:
            adjl[u][v] = 1
            adjl[v][u] = 1
        # global visited
        visited = set()

        def dfs(visited, adjl, node):
            visited.add(node)
            size = 1
            for i in adjl[node]:
                if i not in visited:
                    size += dfs(visited, adjl, i)
            return size
        
        def nc2(n:int)->int:
            if n < 2:
                return 0
            else:
                return (n*(n-1)) // 2
        
        l = []
        for i in range(n):
            if i not in visited:
                l.append(dfs(visited,adjl,i))
        
        total_pairs = (n*(n-1)) // 2
        l2 = [nc2(i) for i in l]
        s = sum(l2)
        return total_pairs-s

        # if not edges:
        #     return (n*(n-1))//2
        # adjl = defaultdict(dict)
        
        # for u, v in edges:
        #     adjl[u][v] = 1
        #     adjl[v][u] = 1
        
        # global visited 
        # visited = set()

        # def dfs(visited, adjl, node):
        #     visited.add(node)
        #     for i in adjl[node]:
        #         if i not in visited:
        #             dfs(visited, adjl, i)
        
        # l = set()
        
        # for i in range(n):
        #     if i not in visited:
        #         dfs(visited, adjl, i)
        #         for node in visited:
        #             for k in range(n):
        #                 if (k not in visited) and ((k, node) not in l) and ((node,k) not in l):
        #                     l.add((node,k))
        #         visited = set()
        # return len(l)