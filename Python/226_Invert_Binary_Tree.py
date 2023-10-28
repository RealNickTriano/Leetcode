from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f" val: {self.val} l:{self.left} r:{self.right}"


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(root: Optional[TreeNode]):
            if root is not None:
                temp = root.left
                root.left = root.right
                root.right = temp

                traverse(root.left)
                traverse(root.right)

        traverse(root)
        return root


sol = Solution()
tree = TreeNode(4,
                TreeNode(2, TreeNode(1), TreeNode(3)),
                TreeNode(7, TreeNode(6), TreeNode(9)))
print(sol.invertTree((tree)))
