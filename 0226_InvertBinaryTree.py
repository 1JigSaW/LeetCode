from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack += node.left, node.right
        return root



root = TreeNode(4)
root.right = TreeNode(7)
root.left = TreeNode(2)
root.left.right = TreeNode(3)
root.left.left = TreeNode(1)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

S = Solution()
print(S.invertTree(root))