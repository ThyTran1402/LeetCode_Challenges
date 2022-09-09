# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0]) # 1st postition in the tree
        mid = inorder.index(preorder[0]) # how many node we want from thhe left subtree
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root

# Preorder: root -> left -> right; root: preorder[0]
# Inorder: left -> root -> right    
# recusion approach
# Time/Space complexity: O(N)