class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k

        def inorder(node):
            if not node:
                return None

            result = inorder(node.left)

            if result is not None:
                return result

            self.k -= 1

            if self.k == 0:
                return node.val

            return inorder(node.right)

        return inorder(root)

        
