# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        mid = 0
        for i in range(len(preorder)):
            if preorder[i] < preorder[0]:
                mid = i
        # mid la vi tri cuoi cung cua nhanh ben tay trai
        if mid > 0:
            root.left = self.bstFromPreorder(preorder[1:mid+1])
        if mid + 1 < len(preorder):
            root.right = self.bstFromPreorder(preorder[mid+1:len(preorder)])
        return root
        
        
        
        
        
#BST: left < node < right
#Preorder: node -> left -> right
#Preorder[0] > x vi tri lien tiep
#Preorder[0] < x vi tri cuoi cung
#x + y + 1 = n

#[8, 5, 1, 7, 10, 12]
#node = 8
#x = 3
#left = [5,1,7]
#x = 3
#y = 2
#right = [10,12]

