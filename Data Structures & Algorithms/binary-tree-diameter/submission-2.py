# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.res = 0

        def dfs(curr):
            if not curr:
                return 0

            self.res = max(self.res, dfs(curr.left) + dfs(curr.right))
            return max(dfs(curr.right) , dfs(curr.left)) + 1
        dfs(root)
        return self.res