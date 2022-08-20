from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        if not root:
            return ''
        queue = deque([root])
        values = []
        while queue:
            cur = queue.popleft()
            if not cur:
                values.append('n')
                continue
            values.append(str(cur.val))
            queue.append(cur.left)
            queue.append(cur.right)
        return ','.join(values)

    def deserialize(self, data):
        if data == '':
            return None
        values = data.split(',')
        root = TreeNode(int(values[0]))
        i = 1
        queue = deque([root])
        while i < len(values):
            cur = queue.popleft()
            if values[i] != 'n':
                cur.left = TreeNode(int(values[i]))
                queue.append(cur.left)
            i += 1
            if values[i] != 'n':
                cur.right = TreeNode(int(values[i]))
                queue.append(cur.right)
            i += 1
        return root
    
