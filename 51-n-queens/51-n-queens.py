class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        positiveDiagonal = set() # r + c
        negativeDiagonal = set() # r - c
        
        result = []
        board = [["."] * n for i in range(n)]
        
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return
            for c in range(n):
                if c in col or (r + c) in positiveDiagonal or (r - c) in negativeDiagonal:
                    continue
                
                col.add(c)
                positiveDiagonal.add(r + c)
                negativeDiagonal.add(r - c)
                board[r][c] = "Q"
                
                backtrack(r + 1)
                
                col.remove(c)
                positiveDiagonal.remove(r + c)
                negativeDiagonal.remove(r - c)
                board[r][c] = "."
                
        backtrack(0)
        return result

# Backtracking algo                
# Time complexity: O(N!)
# Space complexity: O(N^2)