
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        cur  = root
        next = root.left

        while cur.left:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
                cur = cur.next
            else:
                cur = next
                next = cur.left
        return root


root = Node(1)
root.right = Node(3)
root.left = Node(2)
root.left.right = Node(5)
root.left.left = Node(4)
root.right.left = Node(6)
root.right.right = Node(7)
print(Solution().connect(root))