class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        string = ""
        queue = deque([root])
        while queue:
            cur = queue.popleft()
            if not cur:
                string += ",None"
                continue
            else:
                string += "," + str(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
        return string
        
    def deserialize(self, data):
        data = deque(data.split(","))
        _, val = data.popleft(), data.popleft()
        root = None if val == "None" else TreeNode(int(val))
        queue = deque([root])
        while queue:
            cur = queue.popleft()
            if cur:
                a, b = data.popleft(), data.popleft()
                cur.left = TreeNode(int(a)) if a != "None" else None
                cur.right = TreeNode(int(b)) if b != "None" else None
                queue.append(cur.left)
                queue.append(cur.right)
        return root


        
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
ser = Codec()
deser = Codec()
print(ser.serialize(root))
ans = deser.deserialize(ser.serialize(root))