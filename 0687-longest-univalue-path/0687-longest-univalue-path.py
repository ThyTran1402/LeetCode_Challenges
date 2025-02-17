# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        longestPath = [0]
        def traverse(node):
            if not node:
                return 0
            left_length, right_length = traverse(node.left), traverse(node.right)
            left = (left_length + 1) if node.left and node.left.val == node.val else 0
            right = (right_length + 1) if node.right and node.right.val == node.val else 0
            longestPath[0] = max(longestPath[0], left + right)
            return max(left, right)
        traverse(root)
        return longestPath[0]
  
# recurive approach  
# Time/Space complexity: O(N)