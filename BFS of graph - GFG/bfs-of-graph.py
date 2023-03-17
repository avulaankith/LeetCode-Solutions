#User function Template for python3

from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        bfs = []
        visited = [0 for i in range(V+1)]
        distance = [9999999999999999 for i in range(V+1)]
        queue = []
        start = 0
        queue.append(start)
        visited[start] = 1
        distance[start] = 1
        while(len(queue) > 0):
            val = queue[0]
            bfs.append(val)
            queue.pop(0)
            for i in adj[val]:
                if visited[i] == 0:
                    queue.append(i)
                    distance[i] = distance[val] + 1
                    visited[i] = 1
        return bfs
        

#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends