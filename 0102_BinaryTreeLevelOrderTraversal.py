from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # iteratively
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        stack = [root]
        res = []
        while len(stack):
            n = len(stack)
            level = []
            for i in range(n):
                node = stack.pop(0)
                if node.left: 
                    stack.append(node.left)
                if node.right: 
                    stack.append(node.right)
                level.append(node.val)
            res.append(level)
        return res


    # recursively
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def recurse(node, level):
            if not node: 
                return
            if level > len(res): 
                res.append([])
            res[level-1].append(node.val)
            recurse(node.left, level+1)
            recurse(node.right, level+1)
        recurse(root, 1)
        return res

root = TreeNode(3)
root.right = TreeNode(20)
root.left = TreeNode(9)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
root.left.left = TreeNode(155)
root.left.right = TreeNode(755)

S = Solution()
print(S.levelOrder(root))