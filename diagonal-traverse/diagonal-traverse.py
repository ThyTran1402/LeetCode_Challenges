class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        
        res, reverse = [], []
        for diagonal in range(m+n-1):
            reverse.clear()
            r, c = 0 if diagonal < n else diagonal - n + 1, diagonal if diagonal < n else n-1
            while r < m and c > -1:
                reverse.append(mat[r][c])
                r += 1
                c -= 1
            if diagonal % 2 == 0:
                res.extend(reverse[::-1])
            else:
                res.extend(reverse)
        return res