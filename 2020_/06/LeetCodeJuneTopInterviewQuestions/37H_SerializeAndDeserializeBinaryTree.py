#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Runtime: 124 ms, faster than 65.83% of Python3 online submissions for Serialize and Deserialize Binary Tree.
#Memory Usage: 18.6 MB, less than 41.48% of Python3 online submissions for Serialize and Deserialize Binary Tree.


class Codec:

    def serialize(self, root) -> str:
        def pTraverse(root):
            if not root: data.append('#')
            else:
                data.append(root.val)
                pTraverse(root.left)
                pTraverse(root.right)
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        data = []
        pTraverse(root)
        print(data)
        return data


    def deserialize(self, data)->TreeNode:
        if len(data) == 0: return TreeNode(None)
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def pTraverse():
            val = next(dataIter)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = pTraverse()
            node.right = pTraverse()
            return node

        dataIter = iter(data)
        return pTraverse()




class Codec2:

    def serialize(self, root):

        def dfs(root, string):
            if not root:
                return string + 'None,'
            string += str(root.val) + ','
            string = dfs(root.left, string)
            string = dfs(root.right, string)
            return string
        return dfs(root, '')[:-1]       # removing last ','
# Your Codec object will be instantiated and called as such:
codec = Codec()
#codec.deserialize(codec.serialize(root))

tree1 = TreeNode(1)
tree1.left =TreeNode(2)
tree1.right=TreeNode(3)
tree = codec.deserialize(codec.serialize(tree1))

