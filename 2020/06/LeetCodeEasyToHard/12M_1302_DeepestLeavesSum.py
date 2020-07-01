#Runtime: 112 ms, faster than 40.29% of Python3 online submissions for Deepest Leaves Sum.
#Memory Usage: 17.4 MB, less than 19.12% of Python3 online submissions for Deepest Leaves Sum.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import collections

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        sums = collections.defaultdict(list)
        deepest = 0
        def traverse(root, height):
            if root:
                if not root.left and not root.right:
                    nonlocal deepest
                    deepest = max(deepest, height)
                    sums[height] += root.val,
                    return
                traverse(root.left, height+1)
                traverse(root.right, height+1)
        traverse(root, 0)
        return sum([x for _,x in enumerate(sums[deepest])])
    
#Runtime: 104 ms, faster than 56.86% of Python3 online submissions for Deepest Leaves Sum.
#Memory Usage: 17.3 MB, less than 30.37% of Python3 online submissions for Deepest Leaves Sum.
#just do a nonlocal holy hell
class Solution2:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        sums = collections.defaultdict(list)
        deepest = [0]
        def traverse(root, height):
            if root:
                if not root.left and not root.right:
                    deepest[0] = max(deepest[0], height)
                    sums[height] += root.val,
                    return
                traverse(root.left, height+1)
                traverse(root.right, height+1)
        traverse(root, 0)
        return sum([x for _,x in enumerate(sums[deepest[0]])])

node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
s = Solution()
print(s.deepestLeavesSum(node))