class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     if root.val == p and (root.left == q or root.right == q):
    #         return root.val
    #     stack = [(root, None)]
    #     res = []
    #     while stack:
    #         node = stack.pop()
    #         if node[0]:
    #             if node[0].val == p:
    #                 res.append(node)
    #             if node[0].val == q:
    #                 res.append(node)
    #             prev = node
    #             stack.append((node[0].right, node[0].val))
    #             stack.append((node[0].left, node[0].val))
    #     if res[0][1] == res[1][1]:
    #         return res[0][1]
    #     else:
    #         return res[0][0].val

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        parent = {root: None}

        while p not in parent or q not in parent:

            node = stack.pop()

            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        ancestors = set()

        while p:
            ancestors.add(p)
            p = parent[p]

        while q not in ancestors:
            q = parent[q]
        return q

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
p = 5
q = 1
print(Solution().lowestCommonAncestor(root, p, q))