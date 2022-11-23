class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check each row of the board
        for i in range(9):
            currentSet = set() #HashSet to check for duplicates in each row
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in currentSet:
                    return False
                currentSet.add(board[i][j])
                
        #check each column of the board
        for j in range(9):
            currentSet = set() #HashSet to check for duplicates in each col
            for i in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in currentSet:
                    return False
                currentSet.add(board[i][j])
                
        #check each 3x3 sub-box of the board
        for box_x in [0, 1, 2]:
            for box_y in [0, 1, 2]:
                start_x = box_x * 3
                start_y = box_y * 3
                currentSet = set() #HashSet to check for duplicates in each square
                for x in range(start_x, start_x+3):
                    for y in range(start_y, start_y+3):
                        if board[x][y] == '.':
                            continue
                        if board[x][y] in currentSet:
                            return False
                        currentSet.add(board[x][y])
        return True
   
   
#use hashset to check for duplicates in each row, col, and square in the board                     
#Time/Space complexity: O(N^2)