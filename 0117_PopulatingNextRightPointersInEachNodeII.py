# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return
        hashT = defaultdict(list)
        def levelOrd(root, level):
            if root is None:
                return
          
            hashT[level].append(root)
        
            levelOrd(root.left, level+1)
            levelOrd(root.right, level+1)
        
        levelOrd(root, 0)
        
        
        for i in hashT:
            if i == 0:
                continue
            for j in range(0,len(hashT[i])-1):
                hashT[i][j].next = hashT[i][j+1]
        return root


print(Solution().connect(root))