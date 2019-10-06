#### 235-236. 二叉（搜索）树的最近公共祖先
给定一棵二叉(搜索)树，找到该树中两个指定节点的最近公共祖先.
 
最近公共祖先的定义为: "对于有根树T的两个节点p、q，最近公共祖先表示为一个节点x， 满足x是p、q的祖先且x的深度尽可能大(一个节点也可以是它自己的祖先)"

**思路1**：分别找到根节点到p和q的路径，路径中最后一个相同的就是最近公共祖先.
```
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.paths = []
        def findPath(childroot, cur):
            if not childroot or len(self.paths) == 2:
                return
            cur = cur + [childroot]
            if childroot == p or childroot == q:
                self.paths.append(cur)
            findPath(childroot.left, cur)
            findPath(childroot.right, cur)
        findPath(root, [])
        res = None
        mmin = min(len(self.paths[0]), len(self.paths[1]))
        for i in range(mmin):
            if self.paths[0][i] == self.paths[1][i]:
                res = self.paths[0][i]
            else:
                break
        return res
```

**思路2**：递归 
1. 从根节点开始遍历树
2. 如果节点p和q都在右子树上，那么以右孩子为节点继续1的操作
3. 如果节点p和q都在左子树上，那么以左孩子为根节点继续1的操作
4. 如果条件2和条件3都不成立，这就意味着我们已经找到节点p和节点q的LCA了

上述思想参考[https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/solution/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian--2/](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/solution/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian--2/)，但下面代码是自己实现.

```
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right
```

**二叉搜索树的最近公共祖先**

上述讨论了一般二叉树的最近公共祖先，对于二叉搜索树，我们有什么需要改进的呢？

首先考虑二叉搜索树的特性:
+ 对于任意节点n，其左子树上所有节点的值都小于等于节点n的值
+ 其右子树上所有节点的值都大于等于节点n的值

所以有以下算法:
+ 如果根节点大于p和q的值，则在左节点寻找
+ 如果根节点小于p和q的值，则在右节点寻找
+ 其他情况，说明节点p和q一个在左子树， 一个在右子树，lca则是根节点

```
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
```

