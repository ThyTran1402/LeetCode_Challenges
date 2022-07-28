# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#recursive DFS to traverse the tree and check the value
#Time/Space complexity: O(n)

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: # both of them are None
            return True
        
        if not p or not q or q.val != p.val: # only one of them is None, compare the value
            return False
        
        return (self.isSameTree(p.left, q.left) and # call recurively on the left subtree
        self.isSameTree(p.right, q.right)) # call recurively on the right subtree