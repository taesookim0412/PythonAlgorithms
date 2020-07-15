#06-01-2020_

#Follow up: Recursive solution is trivial, could you do it iteratively?
#The Infamous
#The Ambiguous
#The Stack Approach

#Runtime: 24 ms, faster than 91.59% of Python3 online submissions for Binary Tree Inorder Traversal.
#Memory Usage: 13.9 MB, less than 6.56% of Python3 online submissions for Binary Tree Inorder Traversal.
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        contents = []
        stack = []
        curr = root
        while curr or len(stack) > 0:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            contents.append(curr.val)
            curr = curr.right
        return contents





















#Runtime: 28 ms, faster than 74.06% of Python3 online submissions for Binary Tree Inorder Traversal.
#Memory Usage: 13.9 MB, less than 6.56% of Python3 online submissions for Binary Tree Inorder Traversal.
class Solution:
    contents = []
    first = 0
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if self.first == 0:
            self.contents = []
            self.first+=1
        if root:
            self.inorderTraversal(root.left)
            self.contents.append(root.val)
            self.inorderTraversal(root.right)
        return self.contents