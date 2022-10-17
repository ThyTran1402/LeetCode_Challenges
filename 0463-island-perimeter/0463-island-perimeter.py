class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        
        matrix = [0, 1, 0, -1, 0]
        perimeter = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    continue
                perimeter += 4
                for i in range(4):
                    num_r, num_c = r + matrix[i], c + matrix[i + 1]
                    if num_r < 0 or num_r == row or num_c < 0 or num_c == col or grid[num_r][num_c] == 0:
                        continue
                    perimeter -= 1
        return perimeter
 
#counting approach           
#Time complexity: O(M*N)
#Space complexity: O(1)