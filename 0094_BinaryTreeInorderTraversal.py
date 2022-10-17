from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # iteratively
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left

            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        
        return res

    # recursive
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

S = Solution()
print(S.inorderTraversal(root))