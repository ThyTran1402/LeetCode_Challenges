# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #from collections import deque
        result = [] # array for the result
        
        q = collections.deque()
        q.append(root)
        
        while q:
            qLength = len(q) # length of the queue
            level = []
            for i in range(qLength):
                node = q.popleft()
                if node:
                    level.append(node.val) # add node's value to the list level
                    q.append(node.left)
                    q.append(node.right)
            
            if level:
                result.append(level) # add order level to the result list
        return result
        
# BFS approach with queue
# Time complexity: O(N)
# Space complexity: O(N)