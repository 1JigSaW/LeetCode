from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # iteratively
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            curr, val = stack.pop()
            print(stack)
            if not curr.left and not curr.right and val == targetSum:
                return True
            if curr.right:
                stack.append((curr.right, val+curr.right.val))
            if curr.left:
                stack.append((curr.left, val+curr.left.val))
        return False

    # recursively
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None: 
            return False
        
        if root.left is None and root.right is None and root.val == targetSum:
            return True
        
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum-root.val)

root = TreeNode(4)
root.right = TreeNode(7)
root.left = TreeNode(2)
root.left.right = TreeNode(14)
root.left.left = TreeNode(1)
root.right.left = TreeNode(6)
root.right.right = TreeNode(5)
targetSum = 20

S = Solution()
print(S.hasPathSum(root, targetSum))