from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        arr = [root]
        res = []
        while arr:
            
            node = arr.pop()
            res.append(node.val)
            arr.extend(node.children[::-1])
        return res

left = Node(4)
middle = Node(2)
right = Node(1)
right.children = [6,7,8]
root = Node(3)
root.children = [left, middle, right]
print(Solution().preorder(root))
        