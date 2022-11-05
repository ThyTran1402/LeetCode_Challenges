# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        queue = []
        def dfs(node, level):
            if level >= len(queue):
                queue.append(deque([node.val]))
            else:
                if level % 2 == 0:
                    queue[level].append(node.val) #append to the head of the queue
                else:
                    queue[level].appendleft(node.val) #append to the tail of the queue
                    
            for new_node in [node.left, node.right]:
                if new_node is not None:
                    dfs(new_node, level + 1)
        dfs(root, 0)
        return queue
 
#dfs traversal   
#Time complexity: O(N); N is number of nodes in the tree
#Space complexity: O(N)