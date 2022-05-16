from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:  
                stack.append(node.left)
                stack.append(node.right)
                res.append(node.val)
        return res

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

S = Solution()
print(S.postorderTraversal(root))