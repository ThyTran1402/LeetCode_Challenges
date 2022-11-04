class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if len(board) == 0:
            return 0
        m, n = len(board), len(board[0])
        total = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' and (i == 0 or board[i-1][j] == '.') and (j == 0 or board[i][j-1] == '.'):
                    total += 1
        return total

#Time complexity: O(M*N)
#Space complexity: O(1)