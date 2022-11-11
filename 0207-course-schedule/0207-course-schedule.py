class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        for i, j in prerequisites:
            graph[i].append(j)
        def dfs(u):
            if visited[u] == -1:
                return False
            if visited[u] == 1:
                return True
            visited[u] = -1
            for k in graph[u]:
                if not dfs(k):
                    return False
            visited[u] = 1
            return True
        for u in range(numCourses):
            if not dfs(u):
                return False
        return True
    
# Time complexity: O(E+V)-> E: number of courses, V: number of prereq
# Space complexity: O(E+V)