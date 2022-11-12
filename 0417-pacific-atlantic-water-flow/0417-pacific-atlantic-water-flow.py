class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(heights), len(heights[0])
        visitedPacific = [[False for _ in range(n)] for _ in range(m)]
        visitedAtlantic = [[False for _ in range(n)] for _ in range(m)]
        answer = []
        
        for i in range(m):
            self.dfs(heights, i, 0, visitedPacific, m, n)
            self.dfs(heights, i, n-1, visitedAtlantic, m, n)
            
        for j in range(n):
            self.dfs(heights, 0, j, visitedPacific, m, n)
            self.dfs(heights, m-1, j, visitedAtlantic, m, n)
            
        for i in range(m):
            for j in range(n):
                if visitedPacific[i][j] and visitedAtlantic[i][j]:
                    answer.append([i, j])
        return answer
    
    def dfs(self, heights, i, j,visited, m, n):
        visited[i][j] = True
        for direction in self.directions:
            x, y = i+direction[0], j+direction[1]
            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or heights[x][y] < heights[i][j]:
                continue
            self.dfs(heights, x, y, visited, m, n)
            
#DFS recursive
#Time/Space complexity: O(M*N); M is number of rows and N is number of col in the grid
