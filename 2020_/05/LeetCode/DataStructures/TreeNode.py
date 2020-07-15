# -*- coding: utf-8 -*-

from typing import List

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def insertList(self, root, data:List):
        for i, a in enumerate(data):
            if a is None: continue
            node = TreeNode(a)
            self.insert(root, node)
        
    def insert(self, root, node):
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else: self.insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else: self.insert(root.left, node)
    def printInOrder(self, root):
        if root:
            self.printInOrder(root.left)
            print(root.val)
            self.printInOrder(root.right)
            
# root = TreeNode(1)
# root.insertList(root, [1, 2, 3, 4])
# root.printInOrder(root)