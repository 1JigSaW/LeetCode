from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # iteratively
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack1 = [root.left]
        res1 = []
        while stack1:
            node = stack1.pop()
            if node:
                stack1.append(node.left)
                stack1.append(node.right)
                res1.append(node.val)
            else:
                res1.append(None)
        stack2 = [root.right]
        res2 = []
        while stack2:
            node = stack2.pop()
            if node:
                stack2.append(node.right)
                stack2.append(node.left)
                res2.append(node.val)
            else:
                res2.append(None)
        return res1 == res2

    # recursively
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def Symmetric_check(root1, root2):

            if root1 == None and root2 == None:
                return True

            if (root1 != None and root2 != None) and (root1.val == root2.val):
                return Symmetric_check(root1.left, root2.right) and Symmetric_check(root1.right, root2.left)

            return False

        return Symmetric_check(root,root)


root = TreeNode(1)
root.right = TreeNode(2)
root.left = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)

S = Solution()
print(S.isSymmetric(root))