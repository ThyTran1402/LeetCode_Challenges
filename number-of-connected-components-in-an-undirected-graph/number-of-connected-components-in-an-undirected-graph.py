class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #m, n = len(edges), len(edges[0])
        cnt = 0
        graph = [[] for _ in range(n)]
        visited = [False] * n
        #Build adj list 
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node):
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)
                    
                    
        for i in range(n):
            if not visited[i]:
                cnt += 1
                visited[i] = True
                dfs(i)
        return cnt
            
            
            
        