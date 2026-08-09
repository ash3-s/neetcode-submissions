# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(maxv, node):
            if not node:
                return 0
            
            if node.val >= maxv:
                maxv = node.val
            
            return 1 + dfs(maxv, node.left) + dfs(maxv, node.right) if node.val >= maxv else dfs(maxv, node.left) + dfs(maxv, node.right)
        return dfs(root.val, root)

        
