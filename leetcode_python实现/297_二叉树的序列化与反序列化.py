# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        queue = []
        values = []
        queue.append(root)
        while queue:
            top = queue.pop(0)
            if not top:
                values.append('n')
                continue
            values.append(str(top.val))
            queue.append(top.left)
            queue.append(top.right)
        return ','.join(values)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        values = data.split(',')
        root = TreeNode(values[0])
        queue = []
        queue.append(root)
        i = 1
        while queue:
            top = queue.pop(0)
            if not top:
                continue
            if values[i] == 'n':
                top.left = None
            else:
                top.left = TreeNode(int(values[i]))
            queue.append(top.left)
            i += 1
            if values[i].isdigit():
                top.right = TreeNode(values[i])
            else:
                top.right = None
            queue.append(top.right)
            i += 1
        return root

# Your Codec object will be instantiated and called as such:
root = TreeNode(1)
root.left = TreeNode(-1)
root.right = TreeNode(2)
root.left.left = TreeNode(-2)
codec = Codec()
codec.deserialize(codec.serialize(root))