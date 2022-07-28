# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # check if the root is None
        # start from the root
        if not root:
            return None
    
        # swap the children
        temp = root.left
        root.left = root.right
        root.right = temp
        
        self.invertTree(root.left) # recursively invert the left subtree
        self.invertTree(root.right) # recursively invert the right substree
        return root