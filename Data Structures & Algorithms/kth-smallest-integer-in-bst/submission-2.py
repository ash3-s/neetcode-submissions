class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0

        def inorder(node):
            nonlocal count

            if not node:
                return None

            result = inorder(node.left)

            if result is not None:
                return result

            count += 1

            if count == k:
                return node.val

            return inorder(node.right)

        return inorder(root)