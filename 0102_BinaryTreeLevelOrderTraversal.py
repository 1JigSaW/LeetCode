from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans, level = [], [root]
        while level:
            ans.append([node.val for node in level])
            temp = []
            for node in level:
                temp.extend([node.left, node.right])
            level = [leaf for leaf in temp if leaf]
        return ans

root = TreeNode(3)
root.right = TreeNode(20)
root.left = TreeNode(9)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
root.left.left = TreeNode(155)
root.left.right = TreeNode(755)

S = Solution()
print(S.levelOrder(root))