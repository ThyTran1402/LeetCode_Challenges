class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, n, k_mat2 = len(mat1), len(mat1[0]), len(mat2[0])
        
        result = [[0]*len(mat2[0]) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat1[i][j]:
                    for k in range(k_mat2):
                        result[i][k] += mat1[i][j] * mat2[j][k]
        return result
    
#Arrays of arrays
#Time complexity: O(M*N*K)
#Space complexity: O(M*K+K*N)