# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            nonlocal answer
            if node:
                if low <= node.val <= high:
                    answer += node.val
                if low < node.val:
                    dfs(node.left)
                if high > node.val:
                    dfs(node.right)
        answer = 0
        dfs(root)
        return answer
    
# Time complexity: O(N)->N: number of nodes in the tree
# Space complexity: O(N)