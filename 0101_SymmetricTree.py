from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack = [root]
        right = [root.right]
        left = [root.left]
        res1 = []
        res2 = []
        while right:
            node = right.pop()
            if node:
                res1.append(node.val)
                right.append(node.right)
                right.append(node.left)
            else:
                res1.append(None)
        while left:
            node = left.pop()
            if node:
                res2.append(node.val)
                left.append(node.left)
                left.append(node.right)
            else:
                res2.append(None)
            
        print(res1, res2)
        return res1 == res2

root = TreeNode(1)
root.right = TreeNode(2)
root.left = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)
root.left.left = TreeNode(4)
root.left.right = TreeNode(3)

S = Solution()
print(S.isSymmetric(root))