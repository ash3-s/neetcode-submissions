# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.flag = False
        def dfs(curr):
            if not curr: return [True, 0]

            left = dfs(curr.left)
            right = dfs(curr.right)

            
            return [left[0] and right[0] and abs(right[1] - left[1]) <= 1, 1 + max(left[1], right[1])]
        return dfs(root)[0]