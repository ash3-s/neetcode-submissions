class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        n = len(preorder)
        self.idx = 0
        start, end = 0, n - 1

        inorder_hash = {elem:index for index, elem in enumerate(inorder)}

        def dfs(start, end):

            if start > end or self.idx >= n: return None

            root = TreeNode(preorder[self.idx])
            i = inorder_hash[preorder[self.idx]]
            self.idx += 1
            root.left = dfs(start, i - 1)
            root.right = dfs(i + 1, end)
            return root
        
        return dfs(start, end)
        