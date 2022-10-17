from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # iteratively
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return
 
        stack = [root]
        res = []
        while stack:
     
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
     
            if node.right:
                stack.append(node.right)

        return res[::-1]


    # recursive
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        else:
            return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

S = Solution()
print(S.postorderTraversal(root))