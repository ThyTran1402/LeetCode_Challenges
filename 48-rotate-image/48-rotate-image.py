#Time complexity: O(M): M-> number of cells in the grid
#Space complexity: O(1)-> do not use any other additional DS


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        start, end = 0, len(matrix) - 1
        
        while start < end:
            for i in range(end - start):
                top, bottom = start, end
                #save the topLeft
                topLeft = matrix[top][start + i]   
                             
                # move bottom left into top left
                matrix[top][start + i] = matrix[bottom - i][start]
                
                # move bottom right into bottom left
                matrix[bottom - i][start] = matrix[bottom][end - i]
                
                # move top right into bottom right
                matrix[bottom][end - i] = matrix[top + i][end]
                
                # move top left into top right
                matrix[top + i][end] = topLeft
                
            end -= 1
            start += 1