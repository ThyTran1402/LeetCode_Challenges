
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #m, n = len(edges), len(edged[0])
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        q = collections.deque()
        q.append(source)
        visited = set()
        while q:
            curNode = q.popleft()
            if curNode == destination:
                return True
            visited.add(curNode)
            for neighbor in graph[curNode]:
                if neighbor not in visited:
                    q.append(neighbor)
        return False
                
        
    
#BFS
#Time/Space complexity: O(m+n); n is number of nodes' m is number of edges
                    
                    
            
            