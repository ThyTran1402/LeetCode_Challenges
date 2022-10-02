class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # check to ensure len(nums1) > len(nums2)
        if len(nums1) < len(nums2):
            return self.findLength(nums2, nums1)
         
        m, n = len(nums1), len(nums2)
        matrix, prev_matrix = [0] * (n + 1), [0] * (n + 1)
        answer = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    matrix[j] = prev_matrix[j - 1] + 1
                else:
                    matrix[j] = 0
                answer = max(answer, matrix[j])
            matrix, prev_matrix = prev_matrix, matrix
        return answer
    
#DP approach -> Longest Common Substring
#Let matrix[i][j] is the longest common suffix between nums1[0...i-1] and nums2[j...j-1]
#Time complexity: O(M*N); M, N are the length of nums1 and nums2
#Space complexity: O(N)
    
    