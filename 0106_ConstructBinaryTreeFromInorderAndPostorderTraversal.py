from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # recursively
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return
        
        r = postorder.pop() 
        root = TreeNode(r) 
        i = inorder.index(r) 
        root.right = self.buildTree(inorder[i+1:], postorder) 
        root.left = self.buildTree(inorder[:i], postorder) 
        return root

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
print(Solution().buildTree(inorder, postorder))