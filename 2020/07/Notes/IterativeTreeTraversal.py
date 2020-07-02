class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
#https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion-and-without-stack/
#kinda beyond me rn
#https://www.geeksforgeeks.org/level-order-tree-traversal/
#
class Notes():
    def preOrder(self, root):
        if root:
            print(root.val)
            self.preOrder(root.left)
            self.preOrder(root.right)
    def iterateInOrder(self, root):
        inorder = []
        stack = []
        curr = root
        while curr or len(stack) > 0:
            while curr:
                stack += curr,
                curr = curr.left
            curr = stack.pop()
            inorder += curr.val,
            curr = curr.right
        print(inorder)

    def iteratePreOreder(self, root):
        preorder = []
        stack = [root]
        while len(stack)>0:
            curr = stack.pop()
            preorder += curr.val,
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        print(preorder)


#really ugly tree
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
two = tree.left
three = tree.right
two.left = TreeNode(4)
two.right = TreeNode(5)
three.left = TreeNode(6)
three.right = TreeNode(7)

s = Notes()
s.preOrder(tree)
s.iteratePreOreder(tree)
s.iterateInOrder(tree)


