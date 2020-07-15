#Runtime: 36 ms, faster than 38.10% of Python3 online submissions for Sum Root to Leaf Numbers.
#Memory Usage: 14.4 MB, less than 5.04% of Python3 online submissions for Sum Root to Leaf Numbers.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def traverseTree(root, sum):
            if root:
                sum *= 10
                sum += root.val
                print(sum)
                traverseTree(root.left, sum)
                traverseTree(root.right, sum)
                if not root.left and not root.right:
                    self.sum += sum
        self.sum = 0
        traverseTree(root, 0)
        return self.sum

t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)

t2 = TreeNode(1)
t2.left = TreeNode(0)

s = Solution()
#25
#print(s.sumNumbers(t))
print(s.sumNumbers(t2))
