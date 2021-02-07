'''
[再次完整刷 剑指offer 最后一题]

序列化二叉树，没有想到怎么做，翻看了2020年10月份的做题笔记，才看到当时是用层次遍历实现的。

基于思路实现的过程也并不是那么顺利，一个比较大的坑是pop()，默认是pop(-1), 而pop(i)时间复杂度是O(n)，该用list的索引操作

序列化过程，和层次遍历很类似，但需要处理空节点。
反序列化过程，也利用了队列和层次遍历，当遍历到队首元素时，指针i, i+1分别指向队首元素的左右节点的值(这个很巧妙)

这个题目还是有一些细节在里面的:
比如关于空节点和非空节点，在序列化过程中，空节点是加入到队列中， 在反序列化过程中，空节点没有加入到队列中，
设计很巧妙，中间的一些想法还不能很不好理解。
'''

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
            return ''
        q, v = [root], []
        j = 0
        while j < len(q):
            top = q[j]
            j += 1
            if not top:
                v.append('#')
                continue
            v.append(str(top.val))
            q.append(top.left)
            q.append(top.right)
        return '.'.join(v)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        v = data.split('.')
        root = TreeNode(int(v[0]))
        q, i, j = [root], 1, 0
        while j < len(q):
            top = q[j]
            j += 1
            if v[i] != '#':
                top.left = TreeNode(str(v[i]))
                q.append(top.left)
            i += 1
            if v[i] != '#':
                top.right = TreeNode(str(v[i]))
                q.append(top.right)
            i += 1
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))